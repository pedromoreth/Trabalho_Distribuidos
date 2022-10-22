class Cliente:

    def __init__(self, Id):
        self.Id = Id
        self.srv = 0

    def sendMessage(self,remoteId, msg):
        self.srv.receiveMessage(self.Id, remoteId, msg)
        
    def checkMessage(self):
        print(self.srv.getMessage(self.Id))

    def connect(self, serv):
        self.srv = serv

    def desconnect(self):
        self.srv = None


class Server:

    def __init__(self):
        self.pending_msg = {}

    def receiveMessage(self, senderId, receiverId, msg):
        msgkey = senderId + "#" +receiverId
        self.pending_msg.setdefault(msgkey,[]).append(msg)

    
    def getMessage(self, Id):
        for key in self.pending_msg.keys():
            if Id in key:
                return self.pending_msg[key]
        return "Sem mensagem"


    
def Main():

    src = Server()
    cli1 = Cliente("Jose")
    cli1.connect(src)
    cli2 = Cliente("Mariana")
    cli2.connect(src)
    cli3 = Cliente("Pedro")
    cli3.connect(src)
    
    
    cli1.sendMessage("Mariana","teste1")
    cli1.sendMessage("Mariana","teste2")
    cli1.sendMessage("Mariana","teste3")

    cli2.checkMessage()
    cli3.checkMessage()
    
    
    
    cli1.desconnect()
    cli2.desconnect()
    cli3.desconnect()

    

Main()