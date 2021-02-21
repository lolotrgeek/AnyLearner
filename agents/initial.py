# Acts as a Proxy for Reality
# Starts Network by setting initial conditions and spawning agents
# continues to run to spawn new agents
import time
from random import randrange
from modules.publish import Publish, Send, Create, End
from modules.subscribe import Subscribe, Listen, Consume, End
from modules.reply import Reply
from functions.survival import Survival

ENERGY = 1000
NAME = "REALITY"
CHANNEL = Channel(5556)
AGENTS = []

def Distribute(energy):
    """
    randomly assign an energy value
    """
    amount = randrange(0, energy)
    Conserve(amount)
    return amount

def Address():
    """
    Assign an agent an address
    """
    return "tcp://localhost:"+randrange(10000, 20000)

def Spawn(energy):
    """
    Convert energy into agent using random params
    """
    agent = {
        "address": Address() ,
        "life": Distribute(energy),
        "survival" : Survival,
        "actions" : ["reproduce"]
    }
    return agent

def Conserve(energy):
    """
    Energy is never destroyed, only moved
    """    
    global ENERGY
    ENERGY = ENERGY - energy
    return ENERGY


def Spin():
    global ENERGY
    global AGENTS
    print('Spinning...')
    try:
        while ENERGY > 0:
            # spawn agents until all energy has moved to the agents
            agent = Spawn(ENERGY)
            # keep track of agents? 
            AGENTS.append(agent)           
        while True:
            # Send(CHANNEL, NAME, {"energy": ENERGY})
            Listen(CHANNEL,)
            time.sleep(1)
    except:
        print('Closing...')
        End(CHANNEL)
