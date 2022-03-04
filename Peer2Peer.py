import time, socket, sys
 
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('Made by SeenKid#0001')
print('Ton ip est : ',ip)
server_host = input('IP de l\'ami :')
name = input('Nom de l\'ami: ')
myname = input('Ton nom : ')

socket_server.connect((server_host, sport))
 
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' a rejoint le chat...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input(f"{myname} : ")
    socket_server.send(message.encode())  
