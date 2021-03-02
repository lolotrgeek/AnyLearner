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
    """
    channel - tuple : (socket, name)

    callback - function 
    """    
    socket=channel[0]
    try:
        topic = socket.recv_string(flags=zmq.NOBLOCK)
        message = socket.recv_json(flags=zmq.NOBLOCK)
        callback(topic, message)
    except zmq.Again as e:
        # print("No message received yet")
        pass

def Connect(port, name, address="tcp://localhost:"):
    # https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages
    socket = context.socket(zmq.SUB)
    socket.connect(address+str(port))
    socket.subscribe(name)
    socket.setsockopt(zmq.LINGER, 0)
    return socket, name

def End(channel):
    channel[0].close()


def Test():
    CHANNEL = Connect(5556, "TEST")
    def Say(topic, message):
        print(topic)
        print(message)

    try :
        while True:
            Listen(CHANNEL, Say)
    except:
        End(CHANNEL)
if __name__ == "__main__":
    Test()