import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
client_socket("Привет от клиента".encode("utf-8"))
client_socket.close
