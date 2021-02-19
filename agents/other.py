from random import randrange
import sys
sys.path.append('./')
from modules.request import Request
from modules.subscribe import Subscribe

ENERGY = 0
WAIT = 5000

Subscribe("agent0")
Request({"energy": randrange(100)}, WAIT)