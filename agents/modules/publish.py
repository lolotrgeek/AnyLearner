import zmq

# https://dev.to/dansyuqri/pub-sub-with-pyzmq-part-1-2f63#multipart-messages
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

def Publish(channel, message):
    socket.send_string(channel, flags=zmq.SNDMORE)
    socket.send_json(message)

# TEST
# while True:
#     Publish("Hello", {"message": "World"})
#     Publish("Second", {"message": "Topic"})
    
# socket.close()    