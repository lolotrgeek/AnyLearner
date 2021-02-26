import zmq
import time

# TODO: not working...
# bad references, see following...
# https://pyzmq.readthedocs.io/en/latest/api/zmq.html#zmq.Socket.get_monitor_socket
# http://api.zeromq.org/master:zmq-socket-monitor

# need to add following to the socket you want to monitor:
# socket.monitor("inproc://localhost:99999") 

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("inproc://*:99999")
socket.get_monitor_socket()

try:
    while True:
        try:
            event = socket.recv(flags=zmq.NOBLOCK)
            print(event)
            time.sleep(1)
        except zmq.Again as e:
            pass            
except Exception as e:
    print(e)
    socket.close()