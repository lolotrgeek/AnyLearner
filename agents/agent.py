import os, signal, time, argparse, logging
from modules.subscribe import Subscribe, Listen, Connect, End
from modules.publish import Send, Channel, End
from functions.survival import Survival

class Agent:
    def __init__(self, name, address, life, survival, actions, pid=os.getpid):
        self.name = name
        self.address = address
        self.life = life
        self.actions = actions
        self.survival = survival #TODO: type of survival function...
        self.reproductions = []
        self.past_life = []
        self.reality = None
        self.channel = None
        self.pid = pid
        
    def log(self, message):
        logging.debug("%s - %s", self.name, message)

    def Survival(self):
        Survival(self.life, self.past_life, self.reproductions)

    def Hear(self, topic, message):
        """
        Callback to handle subscribed data
        """
        #TODO: if haven't heard from REALITY in x time => Die()
        heard = "Heard : %s %s", self.address, message
        self.log(heard)

    def Die(self):
        os.kill(pid, signal.SIGTERM)

    def Live(self):
        """
        Living is the act of dying.
        """
        if self.life == 0:
            self.Die()
        else:
            Listen(self.reality, self.Hear)
            Send(self.channel, self.name, self.life)            

    def Spin(self):
        self.reality = Connect(5556, "REALITY")
        self.channel = Channel(self.address[1], self.name)
        self.pid = os.getpid()
        print(f"Agent {self.address} Spinning...")
        while True:
            self.Live()
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