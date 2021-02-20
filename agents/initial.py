import time

from modules.publish import Publish, Send, Channel, End
from modules.reply import Reply

ENERGY = 1000
NAME = "AGENT0"

def Response(request):
    if isinstance(request, object) & isinstance(request.get("energy"), int):
        updateEnergy(request.get("energy"))

def updateEnergy(amount):
    global ENERGY
    print(amount)
    if amount < ENERGY:
        ENERGY = ENERGY - amount
        print('new amount:', ENERGY)
        return {"energy": amount}

    else: 
        {"energy": 0}    

# Publish(NAME, {"energy": ENERGY})
channel = Channel(5553)
# channel1 = Channel(5554)

print('Sending...')

try:
    while True: 
        Send(channel, NAME, {"energy": ENERGY})
        # Send(channel1, "TEST", {"test": 1})
        Reply(Response)
        time.sleep(1)
except:
    print('Closing...')
    End(channel)
    # End(channel1)        
