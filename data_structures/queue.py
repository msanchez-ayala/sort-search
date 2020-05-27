"""
A stack is a FIFO (first in first out) data structure. In contrast to a stack, the first element in is also the first one out now.
"""
from .node import node

class Queue:
    def __init__(self, node = None):
        """
        Parameters
        ----------
        node: [Node or None] the node to be first inserted into the queue
        """
        self.top = node
        self.bottom = node

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass