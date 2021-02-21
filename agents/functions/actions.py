
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
