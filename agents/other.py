from random import randrange
from modules.request import Request
from modules.subscribe import Subscribe


ENERGY = 0
WAIT = 5000
CHANNEL = "AGENT0"

messages = []

def say(topic, message):
    print(topic)
    print(message)

print('Listening...') 
Subscribe(CHANNEL, say)

# while True:
#     if(len(messages) > 0):
#         Request({"energy": randrange(100)}, WAIT)
