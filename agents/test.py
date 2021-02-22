from random import randrange
from modules.subscribe import Subscribe, Listen, Connect, End


ENERGY = 0
WAIT = 5000
TOPIC = "REALITY"

channel = Connect(5556, TOPIC)
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
    

End(channel)