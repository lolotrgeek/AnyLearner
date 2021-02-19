import sys
import zmq

context = zmq.Context()

def Subscribe(channel, callback):
    socket = createChannel(channel)
    print("Starting receiver loop ...")
    while True:
        try:
            topic = socket.recv_string(flags=zmq.NOBLOCK)
            message = socket.recv_json(flags=zmq.NOBLOCK)
            callback(topic, message)
        except zmq.Again as e:
            # print("No message received yet")
            pass
    socket.close()
    # context.term()

def createChannel(channel):
    # https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.subscribe(channel)
    socket.setsockopt(zmq.LINGER, 0)
    return socket


# TEST
# Subscribe("Hello")
# Subscribe("Second")
# Unsubscribe("Hello")
