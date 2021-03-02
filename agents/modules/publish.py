import zmq
import time

# https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages

def Publish(topic, message):
    # print('publishing', message)
    socket = Channel(5556, topic)[0]

    print("Starting loop...")
    i = 1
    while True:
        socket.send_string(topic, flags=zmq.SNDMORE)
        socket.send_json(message)
        # print("Sent string: %s ..." % message)
        i += 1
        time.sleep(1)

    End(socket)
    # ctx.term()

def Send(channel, topic, message):
    """
    channel - tuple : (socket, name)
    
    topic - string 

    message - json | string
    """
    socket=channel[0]
    name=channel[1] 
    socket.send_string(topic, flags=zmq.SNDMORE)
    socket.send_json(message)
    # print("Sent string: %s %s ..." % (topic, message))

def Channel(port, name):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind("tcp://*:"+str(port))
    return socket, name

def End(channel):
    channel[0].close()


def Test():
    CHANNEL = Channel(5556, "TEST")
    try:
        while True:
            Send(CHANNEL, "TEST", "Hello!")
            time.sleep(1)
    except:
        End(CHANNEL)

if __name__ == "__main__":
    Test()