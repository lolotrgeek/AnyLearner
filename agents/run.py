import subprocess

life = 0
address = "tcp://localhost:5558"
survival = "survival"
actions = ["action!"]

cmd = f'python agents/agent.py --life {life} --address {address} --survival {survival} --actions {actions}'
subprocess.run(cmd)