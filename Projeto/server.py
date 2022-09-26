import argparse

import redis

# Allow this script to run without installing redisrpc.
sys.path.append('..')
import redisrpc


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

    redis_server = redis.Redis()
    message_queue = 'msg'
    local_object = calc.Calculator()
    server = redisrpc.Server(redis_server, message_queue, local_object)
    server.run()


Main()