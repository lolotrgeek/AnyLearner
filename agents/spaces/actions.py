
# Requests
def request(thing, agent):
    return {'request': thing, 'from': agent }

def give(thing, agent):
    return {'give': thing, 'to': agent}

# Responses
def accept(request):
    return {'response': 'accept'}

def reject(request):
    return {'response': 'reject'}

def connect(address):
    # attempt connection
    # return connection object
    return True

def Reproduce(agents):
    """
    agents pool parameters and energy to create a new agent
    """

    # NOTE:
    # the energy sent goes into the spawned agent
    # spawning agent runs a spawn function 
    # typical spawn function involves parameter cross-over
    # requires energy to run a spawn function

    pass


def Discover():
    # Learns to discover other agents and connect to them
    # has to figure out how to construct address/port strings, starts with characters and numbers

    #NOTE: we can give the agent a human model ( i.e. expert writes if/then statements), the framework needs to be able to take that and adapt it

    CHARACTERS = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m", ":", "/",]
    NUMBERS = [1,2,3,4,5,6,7,8,9,0]

