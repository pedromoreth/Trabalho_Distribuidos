
import argparse
import logging
import traceback
import sys

import redis
sys.path.append('..')
import redisrpc

class Cliente:

    def __init__(self, Id):
        self.Id = Id

    def sendMessage(self,remoteId, msg, server):
        
        
    def checkMessage(self,server):
 
 
    def connect(self, serv):
        self.srv = serv

    def desconnect(self):
        self.srv = None


    
def Main():

    

Main()