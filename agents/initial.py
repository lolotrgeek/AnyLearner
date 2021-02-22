# Acts as a Proxy for Reality
# Starts Network by setting initial conditions and spawning agents
# continues to run to spawn new agents
import time

from random import randrange, randint
from modules.publish import Send, Channel, End
from modules.subscribe import Listen, Connect

from agent import Agent

ENERGY = 1000
NAME = "REALITY"
CHANNEL = Channel(5556, NAME)
AGENTS = []

def Distribute(energy):
    """
    randomly assign an energy value
    """
    amount = randint(1, energy)
    Conserve(amount)
    return amount

def Address():
    """
    Assign an agent an address
    """
    return "tcp://localhost:"+str(randrange(10000, 20000))

def Spawn(energy):
    """
    Convert energy into agent using random params
    """
    agent = Agent(Address(), Distribute(energy), "survival", ["reproduce"])
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
        # spawn agents until all energy has moved to the agents
        while ENERGY > 0:
            print("Spawning...")
            agent = Spawn(ENERGY)
            # keep track of agents? 
            AGENTS.append(agent)

            print(vars(agent))

        while True:
            # Send(CHANNEL, NAME, {"energy": ENERGY})
            Send(CHANNEL, NAME, "Hello!")
            time.sleep(1)

    except Exception as e:
        print('Closing...')
        print(e)
        End(CHANNEL)
Spin()