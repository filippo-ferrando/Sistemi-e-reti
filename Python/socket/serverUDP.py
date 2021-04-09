import socket

ip = "127.0.0.1"
port = 22222
buffer = 4096

#msg = "Messsage from the UDP Server!"
#bytesToSend = str.encode(msg)

udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udpSocket.bind((ip, port))

print("UDP SERVER STARTED")

while True:
    bytesAddressPair = udpSocket.recvfrom(buffer)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientIP)
    print(clientMsg)

    msg = format(message)
    #msg = str(msg)

    bytesToSend = str.encode(msg)

    udpSocket.sendto(bytesToSend, address)