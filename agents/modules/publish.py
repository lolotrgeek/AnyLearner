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

def Send(channel, message):
    socket=channel[0]
    topic=channel[1] 
    socket.send_string(channel, flags=zmq.SNDMORE)
    socket.send_json(message)
    print("Sent string: %s %s ..." % (channel, message))

def Create(port, topic):
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind("tcp://*:"+str(port))
    return socket, topic

def End(channel):
    channel[0].close()

# TEST
# while True:
#     Publish("Hello", {"message": "World"})
#     Publish("Second", {"message": "Topic"})
    
# socket.close()    