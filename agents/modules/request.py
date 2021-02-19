import zmq

context = zmq.Context()

#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
# https://stackoverflow.com/questions/7538988/zeromq-how-to-prevent-infinite-wait

socket.setsockopt(zmq.LINGER, 0)

def Request(message, wait=5000):
    socket.setsockopt(zmq.RCVTIMEO, wait)
    print("Sending request", message)
    socket.send_json(message)

    

    #  Get the reply.
    reply = socket.recv_json()
    print("Received reply %s " % (message))


# TEST
# Request({"message": "Hello"})