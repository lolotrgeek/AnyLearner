# An agent that contains a full observation of all agents 'within'

LIFE = 100

class Listener():
    def __init__(self):
        pass
    def listen(self):
        pass

class Connector():
    def __init__(self):
        pass
    def request(self, agent, resource, amount):
        '''
        send request to another agent
        '''
        pass
    def give(self, agent, resource, amount):
        '''
        send resources to another agent
        '''
        pass
    def accept(self, input):
        '''
        accept an incoming request/gift
        '''
        pass
    def reject(self, input):
        '''
        reject an incoming request/gift
        '''
        pass    
    def disconnect(self, agent):
        '''
        remove connection with an agent
        '''
        pass

class Brain():
    def __init__(self):
        pass

    def learn(self, observations, actions, rewards):
        '''
        learn a survival function by consuming observations and choosing action to optimize survival 
        '''

        # Internal Action Space:
        # choosing modules to turn on/off
        # setting parameters for 'on' modules
        
        # External Action Space: 
        # choosing action from 'on' modules
        # setting parameters for chosen action

    
        func = 0
        return func

    def predict(self, observation):
        '''
        run the survival function to get the next best action (reward prediction) from an observation 
        '''
        action = 0
        return action



class Agent():
    def __init__(self):
        # a "base" agent (environment)

        # VARS
        # state space

        # PROCESS
        # start a loop
        # spin out states each "step" of the loop

        # agents connect to envrionment and consume states
        # environment can accept or reject agents

        # From an "environment-as-agent" perspective:
        # This is the first "agent" in the graph.
        # The second layer of agents derive their states from observing this first agent's states
        # This first agent is attempting to optimize it's survival function.

        # It can take actions.
        # The base actions are to accept/reject incoming connection requests.
        # It must also have a motivation to connect with other agents...

        # I.E. other agents must generate energy, that energy gets added to original agent's "life" value.
        # Otherwise this agent's life will tick away at each timestep.
        # adding to an agent's life value requires the "Give" Method in the connector
        pass
    
    def reset(self):
        pass

    def loop(self, agent):
        pass

    def step(self):
        # tick away life

        # SUB-STEPS:
        # set modules on/off
        # set parameters for 'on' modules

        # get an observation
        # take an action
        # compute reward (run reward function with state action/pairs)

        #NOTE: each sub-step costs life
        pass

    def close(self):
        pass

