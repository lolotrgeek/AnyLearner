from random import randrange
from modules.request import Request
from modules.subscribe import Subscribe, Listen, ConsumeChannel, End


ENERGY = 0
WAIT = 5000
TOPIC = "AGENT0"

channel = ConsumeChannel(5553, TOPIC)
messages = []

# get initial state
# choose action [ publish, subscribe, ... ]
# update state

def say(topic, message):
    print(topic)
    print(message)

print('Listening...') 
while True:
    Listen(channel, say)
    Request({}, WAIT)


End(channel)