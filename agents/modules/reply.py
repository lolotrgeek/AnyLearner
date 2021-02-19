import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def Reply(response):
    #  Wait for next request from client
    request = socket.recv_json()
    print("Received request:", request)

    #  Do some 'work'
    time.sleep(1)
    message = response(request)
    #  Send reply back to client
    socket.send_json(message)

# TEST
# def respond(req):
#     return {"response" : "World"}

# while True:
#     Reply(respond)