import xmlrpc.client
import json

print('\tCLIENTE')


IP = '127.0.0.1'
PORTA = 8085

servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(IP, PORTA))


class Cliente:
    def __init__(self, Id):
        self.Id = Id

    def sendMessage(self,remoteId, msg):
        servidor.receiveMessage(self.Id, remoteId, msg)
        
    def checkMessage(self):
        return json.loads(servidor.getMessage(self.Id))

def Main():

    nome = input("Qual seu nome? ")

    cliente = Cliente(nome)
    
    desejo = 10

    while(desejo!=0):
        print("\nEnviar = 1")
        print("Receber = 2")
        print("fechar = 0")
        desejo = input("Deseja enviar ou receber mensagem? ")

        match desejo:
            case "0":
                print ("\nFinalizando programa")
                desejo=0

            case "1":
                nome = input("\nEnviar para: ")
                msg = input("Mensagem: ")
                cliente.sendMessage(nome, msg)

            case "2":
                mensagem = cliente.checkMessage()
                print("\n", mensagem)

            case default:
                print("\nNúmero errado")


Main()