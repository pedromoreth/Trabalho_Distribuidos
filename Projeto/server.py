from xmlrpc.server import SimpleXMLRPCServer
import json

print('\tSERVIDOR')

chat = {}

class Server:

    def __init__(self):
        self.pending_msg = {}

    def receiveMessage(self,senderId, receiverId, msg):
        msgkey = senderId + "#" +receiverId
        self.pending_msg.setdefault(msgkey,[]).append(msg)
        return True

    def getMessage(self,Id):
        acumulador = None
        chat = {}
        for key in self.pending_msg.keys():
            if "#" + Id in key:
                chat.setdefault(key.split("#")[0],[]).append(self.pending_msg[key])
                  
        if (chat != None):
            return json.dumps(chat)   
                

        return "Sem mensagem"


def Main():


    print('\nEsperando por requisições: ')

    IP = '127.0.0.1'
    PORTA = 8085

    servidor = SimpleXMLRPCServer((IP, PORTA))

    servidor.register_instance(Server())

    servidor.serve_forever()


Main()