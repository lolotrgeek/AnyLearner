import sys
import zmq

channels = []

def Subscribe(channel, messages=[]):
    print('Subscribing...')
    socket = createChannel(channel)
    channels.append([channel, socket])
    print(channels)
    # else:
    #     for channelsocket in channels:
    #         if channelsocket[0] == channel:
    #             # print('Found...')
    #             socket = channelsocket[1]
    #             Listen(socket, messages)
    #         elif i > len(channels):
    #             print('Subscribing...')
    #             socket = createChannel(channel)
    #             channels.append([channel, socket])
    #             print(channels)
    #         else:
    #             print('Seeking...')
    #             i += 1        

def Listen(channel, messages=[]):
    for channelsocket in channels:
        if channelsocket[0] == channel:
            socket = channelsocket[1]
            # print(dir(socket))
            # print(socket.PLAIN_SERVER)
            try:
                topic = socket.recv_string(flags=zmq.NOBLOCK)
                message = socket.recv_json(flags=zmq.NOBLOCK)
                messages.append(message)
                print(topic)
                print(message)
            except zmq.Again as e:
                print("No message received yet")
                pass

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
