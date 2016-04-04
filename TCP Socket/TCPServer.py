import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("127.0.0.1", 8971))
serversocket.listen(2)

print ("Waitting for connection...")

clientsocket, addr = serversocket.accept()
data = clientsocket.recv(1024)
print "Received msg:", data
clientsocket.send("This is from server.")
clientsocket.close()
serversocket.close()
