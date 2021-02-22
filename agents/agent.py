import argparse
from modules.subscribe import Subscribe, Listen, Connect, End
from functions.survival import Survival


class Agent:
    def __init__(self, address, life, survival, actions):
        self.address = address
        self.life = life
        self.actions = actions
        self.survival = "" #TODO: type of survival function...
        self.reality = None
        self.reproductions = []
        self.past_life = []

    def Survival(self):
        Survival(self.life, self.past_life, self.reproductions)

    def Hear(self, topic, message):
        """
        Callback to handle subscribed data
        """
        print("Heard :", message)

    def Spin(self):
        self.reality = Connect(5556, "REALITY")
        print("Spinning...")
        while True:
            Listen(self.reality, self.Hear)

    def Sleep(self):
        End(self.reality)

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