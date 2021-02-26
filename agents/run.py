import subprocess

life = 0
address = "tcp://localhost:5558"
survival = "survival"
actions = ["action!"]

cmd = f'python agents/agent.py --life {life} --address {address} --survival {survival} --actions {actions}'
subprocess.run(cmd)

AGENTS = []

subprocess.run('python Agents/initial.py')
# load each Agent into a sub process
for Agent in AGENTS:
    cmd = f'python Agents/Agent.py --life {Agent.life} --address {Agent.address} --survival {Agent.survival} --actions {Agent.actions}'
    subprocess.run(cmd)