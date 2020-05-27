"""
A stack is a FIFO (first in first out) data structure. In contrast to a stack, the first element in is also the first one out now.
"""
from .node import Node
from .stack import SizeError

class Queue:
    def __init__(self, node = None):
        """
        Parameters
        ----------
        node: [Node or None] the node to be first inserted into the queue
        """
        self.rear = node
        self.front = node

    def enqueue(self, value):
        """
        Adds a new rear node and shifts others down 1.

        Parameters
        ----------
        value: [number or str] The value of the node to be added
        """
        if self.front == None:
            node = Node(value)
            self.front = node
            self.rear = node
        
        else:
            old_rear = self.rear
            new_rear = Node(value)
            old_rear.next = new_rear
            self.rear = new_rear

    def dequeue(self):
        """
        Returns
        -------
        The value of the front node. Also removes that node from the queue.
        """
        old_front = self.front
        new_front = old_front.next
        self.front = new_front
        return old_front.value

    def peek(self):
        """
        Returns
        -------
        The value of the front node WITHOUT removing that node from the queue.
        """
        return self.front.value