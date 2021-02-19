from random import randrange
from modules.request import Request
from modules.subscribe import Subscribe, Listen, Channel, End


ENERGY = 0
WAIT = 5000
TOPIC = "AGENT0"

messages = []

def say(topic, message):
    print(topic)
    print(message)

print('Listening...') 
# Subscribe(CHANNEL, say)

channel = Channel(5553, TOPIC)
channel1 = Channel(5554, "TEST")

while True:
    Listen(channel, say)
    Listen(channel1, say)
    # if(len(messages) > 0):
    #     Request({"energy": randrange(100)}, WAIT)

End(channel)
End(channel1)