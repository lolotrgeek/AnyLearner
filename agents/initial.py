# Acts as a Proxy for Reality
# Starts Network by setting initial conditions and spawning agents
# continues to run to conserve energy and spawn new agents
import os, sys, time, logging, uuid, signal
import psutil
from multiprocessing import Process, Pool
from random import randrange, randint, choice

from modules.publish import Send, Channel, End
from modules.subscribe import Listen, Connect

from agent import Agent
from functions.runonce import run_once

logging.basicConfig(filename='environment.log', format='%(levelname)s %(asctime)s %(message)s', level=logging.DEBUG)


# TODO: reformalize as a class?

NAME = "REALITY"

ENERGY = 1000 # energy held by environment
TOTAL = ENERGY # a constant value set by initial ENERGY
PORTS = []
HEARD = []
CHANNELS = []
AGENTS = []

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

def Conserve(energy):
    """
    Energy is never destroyed, only moved
    """
    global ENERGY
    ENERGY = ENERGY - energy

def Distribute(energy):
    """
    randomly assign an energy value
    """
    return randint(1, energy)

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
    agent = Agent(Name(),  Address(), energy, "survival", ["reproduce"])
    return agent

def Populate():
    """
    Spawn agents until all energy has moved to the agents
    """
    global NAME
    global ENERGY
    global PORTS
    global AGENTS
    global CHANNELS

    try:
        if len(PORTS) == 0:
            print("Generating Ports...")
            GeneratePorts()
        while ENERGY > 0:
            print("Spawning...")
            energy = Distribute(ENERGY)
            Conserve(energy)
            agent = Spawn(energy)
            process = Process(target=agent.Spin, args=())
            print(vars(agent))
            process.start()
            agent.pid = process.pid
            AGENTS.append(agent)
            print('pid:', process.pid)
            CHANNELS.append(Connect(agent.address[1], agent.name))            
            print(NAME, 'Listening to', agent)
    except Exception as e:
        if e:
            print(e)
        else:
            print('Populated...')

def Balance():
    global TOTAL
    global ENERGY
    global AGENTS
    LIFE = []
    for agent in AGENTS:
        LIFE.append(agent.life)

    if len(LIFE) > 0:
        life = sum(LIFE)
        ENERGY = TOTAL - life
        print(f"ENERGY: {ENERGY} / LIFE: {life}") 


def Budget():
    global ENERGY
    if ENERGY > 0:
        logging.warning("Energy available: %s", ENERGY)
        print(f'Energy available: {ENERGY}')
    elif ENERGY < 0:
        logging.error("Energy created ?! %s", ENERGY)
        logging.error("Energy created ?! %s", ENERGY)
    else:
        logging.debug("Energy balanced: %s", ENERGY)

def Hear(topic, message):
    """
    Callback to handle subscribed data
    """
    global HEARD
    global CHANNELS
    logging.debug("Heard : %s, %s", topic, message)
    if topic.find("agent") != -1:
        HEARD.append(topic)

def Remove(item, List):
    """
    Remove an item from a list.
    """
    for index, found in enumerate(List):
        if found == item:
            print("removing:", index, found)
            del List[index]    

def RemoveAgent(agent):
    global AGENTS
    for index, found in enumerate(AGENTS):
        if found.name == agent:
            print("removing:", index, found)
            del AGENTS[index]

def Check(channel):
    """
    Checking for dead agents
    """
    global HEARD
    global CHANNELS
    if channel[1] in HEARD:
        logging.debug("Alive : %s, ", channel[1])
    else:
        print('Died: ', channel[1])
        logging.warning("Died : %s, ", channel[1])
        Remove(channel, CHANNELS)
        RemoveAgent(channel[1])

@run_once
def Prune():
    global AGENTS
    print('Pruning!')
    agent = choice(AGENTS)
    os.kill(agent.pid, signal.SIGTERM) 

def Spin():
    global NAME
    global ENERGY
    global AGENTS
    global HEARD
    CHANNEL = Channel(5556, NAME)
    timeout = 5
    original = len(AGENTS)

    print(NAME, 'Spinning...')

    try:
        run_count = 0
        while True:
            Send(CHANNEL, NAME, "Hello!")

            for channel in CHANNELS:
                Listen(channel, Hear)
                if timeout < run_count:
                    Check(channel)

            # print(f'Number of Agents: {len(AGENTS)} / {original}')
            Balance()
            Budget()
            if timeout < run_count:
                Prune() #TEST
                Populate()
                run_count = 0

            HEARD[:] = []                            
            run_count += 1
            time.sleep(1)

    except Exception as e:
        print(f'Ending {NAME}: {e}')
        logging.error('Ending %s', NAME)
        logging.error(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        End(CHANNEL)
        sys.exit()


    
if __name__ == "__main__":
    ENVID = os.getpid()
    Populate()
    Spin()


