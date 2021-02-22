
from modules.subscribe import Subscribe, Listen, Connect, End

def Listener(self, topic, message):
    """
    Callback to handle subscribed data
    """
    print("Heard :", message)

class Agent:
    def __init__(self, address, life, Survival, actions):
        self.address = address
        self.life = life
        self.actions = actions
        self.Survival = Survival 
        self.reality = Connect(5556, "REALITY")

    def Spin(self):
        while True:
            Listen(self.reality, Listener)

    def Sleep(self):
        End(self.reality)