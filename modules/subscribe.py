import sys
import zmq

# https://zguide.zeromq.org/docs/chapter1/#Getting-the-Message-Out
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

def Subscribe(channel):
    socket.setsockopt_string(zmq.SUBSCRIBE, channel)
    string = socket.recv_string()
    print(string)

Subscribe("Hello")