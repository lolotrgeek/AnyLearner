# Populate Environment by spawning agents into sub-processes
import subprocess
import os
import sys
from multiprocessing import Process, Pool
import initial

#TODO: wrapper to check PID's for each spawned process

# subprocess.run('python Agents/initial.py')
# # load each Agent into a sub process
# for Agent in AGENTS:
#     cmd = f'python Agents/Agent.py --life {Agent.life} --address {Agent.address} --survival {Agent.survival} --actions {Agent.actions}'
#     subprocess.run(cmd)

if __name__ == '__main__':
    ENVID = os.getpid()
    AGENTS = []
    processes = []
    try:
        initial.Populate(AGENTS)
    except Exception as e:
        print(e)
        sys.exit()
    
    try:
        processes.append(Process(target=initial.Spin, args=()))

        for Agent in AGENTS:
            processes.append(Process(target=Agent.Spin, args=()))
        
        for p in processes:
            print(p)
            p.start()
    except Exception as e:
        print(e)
        sys.exit()