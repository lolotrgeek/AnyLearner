import sys
import zmq

# https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages

def Subscribe(channel):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.setsockopt_string(zmq.SUBSCRIBE, channel)
    topic = socket.recv_string()
    message = socket.recv_json()
    print(topic)
    print(message)

# TEST
# Subscribe("Hello")
# Subscribe("Second")
