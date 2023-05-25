import os 
from socket import * 

def send_to_server(message, server, addr):
    server.sendto(bytes(name, 'utf-8'), addr)
    server.sendto(bytes(message, 'utf-8'), addr)

def init(name, server):
    server.sendto(bytes("!$!$", 'utf-8'), main_addr)
    server.sendto(bytes(name, 'utf-8'), main_addr)
    
def receive_message(server, buf = 1024):
    
    (data1, addr) = server.recvfrom(buf)
    print("1")
            
    print(str(data1, 'utf-8'))


name = input("Please enter your name：")

main_host = "10.135.187.95" # set to IP address of target computer 
port = 13000 
main_addr = (main_host, port) 

UDPSock = socket(AF_INET, SOCK_DGRAM)

init(name, UDPSock)

while True:
    message = input("input message：")
    send_to_server(message, UDPSock, main_addr)    
    receive_message(UDPSock)
    

UDPSock.close() 
os._exit(0) 