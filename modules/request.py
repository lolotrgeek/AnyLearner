import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
def Request(message):
    print("Sending request", message)
    socket.send_json(message)

    #  Get the reply.
    reply = socket.recv_string()
    print("Received reply %s [ %s ]" % (reply, message))

Request({"message": "Hello"})