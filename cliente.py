import socket

HOST = '127.0.0.1'

PORT = 50000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST , PORT)) #! passando o host e a porta para conectar no servidor

s.sendall(str.encode('Bom dia Tropa!')) #! comando para enviar dados pro servidor

data = s.recv(1024)

print('Mensagem recebida porra:', data.decode())