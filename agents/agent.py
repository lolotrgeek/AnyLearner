import argparse
import time
import os
from modules.subscribe import Subscribe, Listen, Connect, End
from modules.publish import Send, Channel, End
from functions.survival import Survival


class Agent:
    def __init__(self, name, address, life, survival, actions):
        self.name = name
        self.address = address
        self.life = life
        self.actions = actions
        self.survival = survival #TODO: type of survival function...
        self.reproductions = []
        self.past_life = []
        self.reality = None
        self.channel = None
        self.pid = os.getpid()

    def Survival(self):
        Survival(self.life, self.past_life, self.reproductions)

    def Hear(self, topic, message):
        """
        Callback to handle subscribed data
        """
        print("Heard :", self.address, message)

    def Spin(self):
        self.reality = Connect(5556, "REALITY")
        self.channel = Channel(self.address[1], self.name)
        self.pid = os.getpid()
        print("Agent Spinning...")
        while True:
            Listen(self.reality, self.Hear)
            Send(self.channel, "energy", self.life)
            time.sleep(1)

    def Sleep(self):
        End(self.reality)
        End(self.channel)

# Run an agent with command line args.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run an agent with command line args.')
    parser.add_argument('--address', help='String, network address ie: "tcp://localhost:5000"')
    parser.add_argument('--life', help='Integer, represents life value of agent')
    parser.add_argument('--survival', help='Function, for determining rewards')
    parser.add_argument('--actions', help='List, possible actions')

    args = vars(parser.parse_args())
    # for arg in args:
    #     print(type(arg), arg)
    
    address = args.get("address")
    life = int(args.get("life"))
    survival = args.get("survival")
    actions = args.get("actions").split(',')

    print("address", type(address), address)
    print("life ",type(life), life)
    print("survival ", type(survival), survival)
    print("actions " , type(actions), actions)

    agent = Agent(address, life, survival, actions)

    try:
        agent.Spin()
    except:
        agent.End()