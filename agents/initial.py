import time

from modules.publish import Publish, Send, Channel, End
from modules.reply import Reply

ENERGY = 1000
NAME = "AGENT0"

# # def Response(request):
# #     if isinstance(request, object) & isinstance(request.get("energy"), int):
# #         # print(request.get("energy"))
# #         if request.get("energy") < ENERGY:
# #             return {"energy": request.get("energy")}
# #     else:
# #         return {"energy": 0}


# Publish(NAME, {"energy": ENERGY})
channel = Channel(5553)
channel1 = Channel(5554)

print('Sending...')

try:
    while True: 
        Send(channel, NAME, {"energy": ENERGY})
        Send(channel1, "TEST", {"test": 1})
        time.sleep(1)
except:
    print('Closing...')
    End(channel)
    End(channel1)        
