import threading
import socket

lock = threading.Lock()
clients = []

def broadcast_message(message, sender_socket=None):
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    continue

def handle_client(client_socket, client_address):
    print(f"Клиент {client_address} подключён")

    welcome_message = f"Добро пожаловать в чат! Ваш адрес: {client_address}"
    client_socket.send(welcome_message.encode("utf-8"))

    join_message = f"Пользователь {client_address} присоединился к чату"
    broadcast_message(join_message, client_socket)
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
                
            message = data.decode("utf-8")
            print(f"{client_address}: {message}")

            formatted_message = f"{client_address}: {message}"
            broadcast_message(formatted_message, client_socket)
            
        except:
            break

    with lock:
        if client_socket in clients:
            clients.remove(client_socket)

    leave_message = f"Пользователь {client_address} покинул чат"
    broadcast_message(leave_message)
    
    client_socket.close()
    print(f"Клиент {client_address} отключился")

def start_server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(("127.0.0.1", 5000))
    socket_server.listen()
    
    print("Сервер запущен на 127.0.0.1:5000")
    print("Ожидание подключения клиентов...")
    
    try:
        while True:
            client_socket, client_address = socket_server.accept()
            with lock:
                clients.append(client_socket)
            
            th = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
            th.start()
            
    except KeyboardInterrupt:
        print("\nСервер останавливается...")
        with lock:
            for client in clients:
                try:
                    client.close()
                except:
                    pass
        socket_server.close()

if __name__ == "__main__":
    start_server()