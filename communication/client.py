import os 
from socket import * 
host = "10.118.175.78" # set to IP address of target computer 
port = 13000 
addr = (host, port) 
UDPSock = socket(AF_INET, SOCK_DGRAM) 
while True: 
    data = input("Enter message to send or type 'exit': ")
    data = bytes(data, 'utf-8') 
    UDPSock.sendto(data, addr) 
    if data == "exit": 
        break 
UDPSock.close() 
os._exit(0) 