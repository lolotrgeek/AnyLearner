import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


def Reply():
    #  Wait for next request from client
    message = socket.recv_json()
    print("Received request:", message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("World")

while True:
    Reply()