import sys
import zmq

channels = []

def Subscribe(channel):
    print('Subscribing...')
    try:
        socket = createChannel(channel)
        channels.append([channel, socket])
        print(channels)
        topic = socket.recv_string(flags=zmq.NOBLOCK)
        message = socket.recv_json(flags=zmq.NOBLOCK)
        print(topic)
        print(message)
    except zmq.Again as e:
        print ("No message received yet")    

def Unsubscribe(channel):
    print('Unsubscribing...')
    for index, channelsocket in enumerate(channels):
        if channelsocket[0] == channel:
            print('closing socket...')
            socket = channelsocket[1]
            socket.close()
            del channels[index]
            print(channels)   


def createChannel(channel):
    # https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages    
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5556")
    socket.setsockopt_string(zmq.SUBSCRIBE, channel)
    socket.setsockopt(zmq.LINGER, 0)
    return socket

# TEST
# Subscribe("Hello")
# Subscribe("Second")
# Unsubscribe("Hello")