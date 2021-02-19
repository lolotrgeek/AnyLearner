import zmq
import time

# https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages

def Publish(channel, message):
    # print('publishing', message)
    socket = Channel(5556)

    print("Starting loop...")
    i = 1
    while True:
        socket.send_string(channel, flags=zmq.SNDMORE)
        socket.send_json(message)
        print("Sent string: %s ..." % message)
        i += 1
        time.sleep(1)

    End(socket)
    # ctx.term()

def Send(socket, channel, message):
    socket.send_string(channel, flags=zmq.SNDMORE)
    socket.send_json(message)
    print("Sent string: %s %s ..." % (channel, message))

def Channel(port):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind("tcp://*:"+str(port))
    return socket

def End(socket):
    socket.close()

# TEST
# while True:
#     Publish("Hello", {"message": "World"})
#     Publish("Second", {"message": "Topic"})
    
# socket.close()    