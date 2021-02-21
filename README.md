# Any Learner
simple, early messaging framework for functional/modular learners

## Goals
- minimal --> small human encoded [rulial space](https://writings.stephenwolfram.com/2020/06/exploring-rulial-space-the-case-of-turing-machines/)
- functional framework that represents future hardware designs
- let machines encode rules/parameters
- emergent functionality, learn via "survival as a function"
- learned network topologies
- local peer-to-peer, sparse connectivity (nodes are not fully connected)

## Messaging
Channel --> Topics --> Messages 

A Channel binds to a port. 

A Channel can have multiple topics.

Topics can have multiple messages.


## TODO:
- pub/sub: non-blocking individual channels?
- pub/sub: [implement udp?](https://zguide.zeromq.org/docs/chapter8/#Cooperative-Discovery-Using-UDP-Broadcasts)