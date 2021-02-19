import zmq
import time

# https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages

def Publish(channel, message):
    # print('publishing', message)
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.bind("tcp://*:5556")

    print("Starting loop...")
    i = 1
    while True:
        sock.send_string(channel, flags=zmq.SNDMORE)
        sock.send_json(message)
        print("Sent string: %s ..." % message)
        i += 1
        time.sleep(1)

    sock.close()
    ctx.term()


# TEST
# while True:
#     Publish("Hello", {"message": "World"})
#     Publish("Second", {"message": "Topic"})
    
# socket.close()    