# Populate Environment by spawning agents into sub-processes
import os, sys, time, logging
import psutil
from multiprocessing import Process, Pool
import initial

logging.basicConfig(filename='environment.log', format='%(levelname)s %(asctime)s %(message)s', level=logging.DEBUG)

#TODO: agents dying can be done with wrapper to check PID's for each spawned process, when agent energy = 0 kill PID

def Populate(agents):
    try:
        initial.Populate(agents)
    except Exception as e:
        logging.warning(e)
        sys.exit()

def Spin(agents, processes):
    try:
        processes.append(Process(target=initial.Spin, args=(agents, )))

        for Agent in agents:
            processes.append(Process(target=Agent.Spin, args=()))
        
        for p in processes:
            print(p)
            p.start()
            print('pid:', p.pid)
    except Exception as e:
        logging.error(e)
        sys.exit()    

def Alive(agents):
    while True:
        for agent in agents:
            print('Alive:', agent.pid)
            if agent.pid is not None:
                if psutil.pid_exists(agent.pid):
                    print('Life:' , agent.life)
                else:
                    print("Dead: ", agent.pid )
        time.sleep(1)

if __name__ == '__main__':
    ENVID = os.getpid()
    AGENTS = []
    processes = []
     
    Populate(AGENTS)
    Spin(AGENTS, processes)
