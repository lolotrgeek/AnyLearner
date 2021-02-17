import zmq

# https://zguide.zeromq.org/docs/chapter1/#Getting-the-Message-Out
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

def Publish(message):
    socket.send_string(message)


while True:
    Publish("Hello")