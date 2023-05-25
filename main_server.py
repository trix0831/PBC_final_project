import os 
from socket import * 
import player
import get_ip

def receive_message(server, buf = 1024):
    (data1, addr) = server.recvfrom(buf)
    (data2, addr) = server.recvfrom(buf)
    
    data1 = str(data1, 'utf-8')
    data2 = str(data2, 'utf-8')

    if data2 == "!$!$":
        player_list.append(player.Player([], [], [], data2, addr))
        print("player added")
    else:
        print("here")
        print(str(data1) + "：" + str(data2))
        broadcast(player_list, server, str(data1) + "：" + str(data2))

def send_message_to_client(server, addr_target, message):
    server.sendto(bytes(message, 'utf-8'), addr_target)
    
def broadcast(player_list, server, message):
    for player in player_list:
        server.sendto(bytes(message, 'utf-8'), player.addr)
    

host = get_ip.get_wifi_ipv4_address()
port = 13000 
buf = 1024 

addr = (host, port) 

UDPSock = socket(AF_INET, SOCK_DGRAM) 
UDPSock.bind(addr)

player_list = []

print("Waiting to receive messages...")

while True: 
    receive_message(UDPSock, buf)
    
UDPSock.close() 
os._exit(0) 