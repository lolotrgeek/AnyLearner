# Acts as a Proxy for Reality
# Starts Network by setting initial conditions and spawning agents
# continues to run to conserve energy and spawn new agents
import sys, os, time, uuid, logging
from random import randrange, randint, choice
from modules.publish import Send, Channel, End
from modules.subscribe import Listen, Connect

from agent import Agent

ENERGY = 1000
LIFE = [] # energy held by agents
PORTS = []

def GeneratePorts():
    global PORTS
    while len(PORTS) < 1000:
        port = randrange(10000, 20000)
        if port not in PORTS:
                PORTS.append(port)

def ChoosePort():
    """
    Choose a port from list, remove it from list and return
    """
    global PORTS
    port = choice(PORTS)
    PORTS.remove(port)
    if port not in PORTS:
        return port

def Distribute(energy):
    """
    randomly assign an energy value
    """
    amount = randint(1, energy)
    Conserve(amount)
    return amount

def Address():
    """
    Assign address to agent
    """ 
    return "tcp://localhost:", ChoosePort()

def Name():
    return "agent_"+uuid.uuid4().hex    

def Spawn(energy):
    """
    Convert energy into agent using random params
    """
    agent = Agent(Name(),  Address(), Distribute(energy), "survival", ["reproduce"])
    return agent

def Populate(agents):
    """
    Spawn agents until all energy has moved to the agents
    """
    global ENERGY
    global PORTS
    global LIFE
    try:
        if len(PORTS) == 0:
            GeneratePorts()      
        while ENERGY > 0:
            print("Spawning...")
            agent = Spawn(ENERGY)
            agents.append(agent)
            # Add life now...
            # LIFE.append(vars(agent).get("life"))
            # print(LIFE)
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

def Balance():
    global ENERGY
    global LIFE
    if len(LIFE) > 0:
        total = sum(LIFE)
        energy = ENERGY - total
        return energy
    else:
        return 0

def Budget(agents):
    budget = Balance()
    if budget > 0:
        logging.warn("Energy available: %s",budget)
        print(f'Energy available: {budget}')
    elif budget < 0:
        logging.error("Energy created ?! %s", budget)
    else:
        logging.debug("Energy balanced: %s", budget)    

def Spend(energy, agents):
    """
    Spend available energy
    """
    agent = Spawn(energy)
    agents.append(agent)
    print("Spawning:",  vars(agent))    

def Hear(topic, message):
    """
    Callback to handle subscribed data
    """
    global LIFE
    logging.debug("Heard : %s, %s", topic, message)
    if topic.find("agent") != -1:
        print(topic)
        LIFE.append(message)

def Spin(agents):
    global ENERGY
    global LIFE
    NAME = "REALITY"
    CHANNEL = Channel(5556, NAME)
    channels = []
    
    for agent in agents:
        print(NAME, 'Listening to', agent)
        channels.append(Connect(agent.address[1], agent.name))

    print(NAME, 'Spinning...')
    try:
        while True:
            Send(CHANNEL, NAME, "Hello!")

            # TODO: remove channel of agents that have disconnected
            # TODO: wait to remove channels after running Populate()
            
            for channel in channels:
                Listen(channel, Hear)
            print(LIFE)
            Budget(agents)
            LIFE[:] = []
            time.sleep(1)

    except Exception as e:
        print(f'Ending {NAME}: {e}')
        logging.error('Ending %s', NAME)
        logging.error(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)        
        End(CHANNEL)

if __name__ == "__main__":
    # Populate(AGENTS)
    Spin()