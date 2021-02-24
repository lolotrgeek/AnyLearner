from random import randrange, choice
ADDRESSES = []

def Addressing():
    global ADDRESSES
    print('Addressing...')
    while len(ADDRESSES) < 1000:
        address = randrange(10000, 20000)
        if address not in ADDRESSES:
            ADDRESSES.append(address)

Addressing()
# print(ADDRESSES)

address = choice(ADDRESSES)
print(address)
ADDRESSES.remove(address)
print(len(ADDRESSES))
if address not in ADDRESSES:
    print(address)
