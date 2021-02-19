from random import randrange
import sys
sys.path.append('./')
from modules.request import Request

ENERGY = 0
WAIT = 5000

Request({"energy": randrange(100)}, WAIT)
