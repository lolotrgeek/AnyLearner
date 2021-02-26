# Acts as a Proxy for Reality
# Starts Network by setting initial conditions and spawning agents
# continues to run to conserve energy and spawn new agents
import time, uuid, logging
from random import randrange, randint, choice
from modules.publish import Send, Channel, End
from modules.subscribe import Listen, Connect

from agent import Agent

ENERGY = 1000
ENERGIES = []
ADDRESSES = []


def Distribute(energy):
    """
    randomly assign an energy value
    """
    amount = randint(1, energy)
    Conserve(amount)
    return amount

def Port():
    """
    Choose a port from list, remove it from list and return
    """
    global ADDRESSES
    address = choice(ADDRESSES)
    ADDRESSES.remove(address)
    if address not in ADDRESSES:
        return address

def Address():
    """
    Assign an agent an address
    """
    return "tcp://localhost:", Port() 

def Name():
    return "agent_"+uuid.uuid4().hex    

def Spawn(energy):
    """
    Convert energy into agent using random params
    """
    agent = Agent(Name(), Address(), Distribute(energy), "survival", ["reproduce"])
    return agent

def Populate(agents):
    global ENERGY
    global ADDRESSES
    try:
        # Generate unique list of addresses
        print('Addressing...')
        while len(ADDRESSES) < 1000:
            address = randrange(10000, 20000)
            if address not in ADDRESSES:
                ADDRESSES.append(address)          
        # spawn agents until all energy has moved to the agents
        while ENERGY > 0:
            print("Spawning...")
            agent = Spawn(ENERGY)
            # keep track of agents? 
            agents.append(agent)
            print(vars(agent)) 
    except Exception as e:
        if e:
            print(e)
        else:
            print('Populated...')
        
def Conserve(energy):
    """
    Energy is never destroyed, only moved
    """    
    global ENERGY
    ENERGY = ENERGY - energy
    return ENERGY

def Transact(energies):
    energy = sum(energies)
    total = ENERGY - energy
    if total > 0:
        logging.warn("Energy was Created!? %s",total)
    elif total < 0:
        logging.warn("Energy is left over: %s", total)
    else:
        logging.debug("Energy is balanced: %s", total)

def Hear(topic, message):
    """
    Callback to handle subscribed data
    """
    global ENERGIES
    logging.debug("Heard : %s, %s", topic, message)
    if topic == "energy":
        ENERGIES.append(message)

def Spin(agents):
    global ENERGY
    NAME = "REALITY"
    CHANNEL = Channel(5556, NAME)
    channels = []
    
    for agent in agents:
        print(NAME, 'Listening to', agent)
        channels.append(Connect(agent.address[1], "energy"))

    print(NAME, 'Spinning...')
    try:
        while True:
            # Send(CHANNEL, NAME, {"energy": ENERGY})
            Send(CHANNEL, NAME, "Hello!")
            for channel in channels:
                Listen(channel, Hear)

            Transact(ENERGIES)
            ENERGIES[:] = []
            time.sleep(1)

    except Exception as e:
        print('Closing...')
        print(e)
        End(CHANNEL)

if __name__ == "__main__":
    # Populate(AGENTS)
    Spin()