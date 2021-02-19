import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
socket.setsockopt(zmq.LINGER, 0)


def Reply(response):
    try:
        #  Wait for next request from client
        request = socket.recv_json(flags=zmq.NOBLOCK)
        print("Received request:", request)

        #  Do some 'work'
        time.sleep(1)
        message = response(request)
        #  Send reply back to client
        socket.send_json(message)
    except zmq.Again as e:
        # print ("No message received yet")
        pass
# TEST
# def respond(req):
#     return {"response" : "World"}

# while True:
#     Reply(respond)