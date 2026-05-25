import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(message.decode("utf-8"))
        except:
            print("Соединение с сервером потеряно")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode("utf-8"))
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect(("127.0.0.1", 5000))
        print("Подключено к серверу чата")
    except:
        print("Не удалось подключиться к серверу")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)
    send_thread.start()
    
    try:
        send_thread.join()
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()