'''
telefono senza fili in python
'''
import socket as sck

HOST_CLIENT = ('x.x.x.x', 4096)
HOST_SERVER = ('0.0.0.0', 4096)

def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    
    server.bind(HOST_SERVER)

    data, addr = server.recvfrom(4096)
    print(data.decode())
    client.sendto(data.encode(), HOST_CLIENT)
    
    server.close()
    client.close()

if __name__ == '__main__':
    main()