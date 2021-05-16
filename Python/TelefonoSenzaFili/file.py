'''
telefono senza fili in python
'''
import socket as sck


HOST_CLIENT = ('192.168.0.131', 7000)
HOST_SERVER = ('192.168.0.133', 7000)

def main():
    server.bind(HOST_SERVER)
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    while True:
        data, addr = server.recvfrom(4096)
        print(data.decode())
        client.sendto(data, HOST_CLIENT)
        
        server.close()
        client.close()

if __name__ == '__main__':
    main()