import socket

serverAddress = ("127.0.0.1", 22222)
buffer = 4096
udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input()
    bytesToSend = str.encode(msg)
    udpSocket.sendto(bytesToSend, serverAddress)

    msgFromServer = udpSocket.recvfrom(buffer)

    msgPrint = "Message from Server {}".format(msgFromServer[0])
    print(msgPrint)
