from random import randrange
from modules.request import Request
from modules.subscribe import Subscribe, Listen


ENERGY = 0
WAIT = 5000

messages = []
Subscribe("agent0")
while True:
    Listen("agent0", messages)
    if(len(messages) > 0):
        Request({"energy": randrange(100)}, WAIT)