#!/usr/bin/env python3
import socket
from urllib import request


HOST = 'localhost'

PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #! criando o socket

s.bind((HOST, PORT)) #! passando o host e a porta

s.listen() #! modo de escuta

print('Aguardando conexão de um cliente')

conn , ender = s.accept() #! metodo para aceitar a conexão

print('Conectado em', ender) #! mostra a porta que está conectado

while True:
    data = conn.recv(1024) #! tamanho maximo de bites que posso receber
    if not data:
        print('Fechando a conexão...')
        conn.close()
        break
    conn.sendall(data) #! enviando de volta os dados.
