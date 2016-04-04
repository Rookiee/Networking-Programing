import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "Hello, this is udp client!"
clientSocket.sendto(data, ('127.0.0.1', 9000))

clientSocket.close()
