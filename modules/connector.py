# Let the Machine build it's own protocol!
# starts with initial values, then learns new values via rewards

# DECISION: add peer to list?
# DECISION: what IP/port to use
# DECISION: how many times to ping?
# DECISION: accept/reject?

import os
import socket
import sys
import time

import zmq


TCP_HOST = "127.0.0.1"
TCP_PORT = 65432

UDP_HOST = "127.0.0.1"
UDP_PORT = 5005


def Send(message):
    pass


def Connect(peer):
    """
    Parameters
    ----------
    peer : tuple 
        (address, port)
    """
    pass



# req/res over TCP


def Request(peer, request):
    pass

def Response(peer, response):
    pass


# pub/sub over UDP
def Publish(message):
    pass


def Subscribe():

    pass
