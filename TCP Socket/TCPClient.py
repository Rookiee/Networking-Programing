import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1", 8971))

clientSocket.send("Hello, This is from client")
data = clientSocket.recv(1024)
print "Received msg:", data

clientSocket.close()
