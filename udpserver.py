from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('Server waiting ready.')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('New client sent message.')
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
    print('Replied sent to client.')
