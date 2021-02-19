
import sys
import signal
import time

from modules.publish import Publish
from modules.reply import Reply

ENERGY = 1000
NAME = "AGENT0"


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)


def Start():
    print('Listening...')
    while True:
        Reply(Response)
        Publish(NAME, {"energy": ENERGY})


def Response(request):
    if isinstance(request, object) & isinstance(request.get("energy"), int):
        print(request.get("energy"))
        if request.get("energy") < ENERGY:
            return {"energy": request.get("energy")}
    else:
        return {"energy": 0}


Start()
