import sys
import zmq


context = zmq.Context()

def Subscribe(topic, callback):
    socket = Connect(5556, topic)[0]
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


def Listen(channel, callback):
    socket=channel[0]
    try:
        topic = socket.recv_string(flags=zmq.NOBLOCK)
        message = socket.recv_json(flags=zmq.NOBLOCK)
        callback(topic, message)
    except zmq.Again as e:
        # print("No message received yet")
        pass

def Connect(port, topic, address="tcp://localhost:"):
    # https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages
    socket = context.socket(zmq.SUB)
    socket.connect(address+str(port))
    socket.subscribe(topic)
    socket.setsockopt(zmq.LINGER, 0)    
    return socket, topic

def End(channel):
    channel[0].close()

# TEST
# Subscribe("Hello")
# Subscribe("Second")
# Unsubscribe("Hello")
