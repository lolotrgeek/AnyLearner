
import subprocess
import os
from multiprocessing import Process, Pool
import initial


AGENTS = []
PROCESSES = []

initial.Populate(AGENTS)

# subprocess.run('python Agents/initial.py')
# # load each Agent into a sub process
# for Agent in AGENTS:
#     cmd = f'python Agents/Agent.py --life {Agent.life} --address {Agent.address} --survival {Agent.survival} --actions {Agent.actions}'
#     subprocess.run(cmd)

if __name__ == '__main__':
    PROCESSES.append(Process(target=initial))

    for Agent in AGENTS:
        PROCESSES.append(Process(target=Agent))
    
    for p in PROCESSES:
        print(p)
        p.start()
