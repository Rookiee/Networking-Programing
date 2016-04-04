import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 9000))

data, addr = serverSocket.recvfrom(1024)

print 'Received msg is %s' % (data)
print 'the type of addr is ', type(addr)
print 'addr', addr

serverSocket.close()
