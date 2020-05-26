"""
A stack is a LIFO (last in first out) structure. The most recently added element
is the first one that can be seen or removed.

We use the basic node model containing a value and a reference to the next node 
(node below current one in the stack)
"""
from .node import Node

class Stack:
    def __init__(self, node = None, capacity = 10):
        """
        Parameters
        ----------
        node: [Node or None] Node to be instantiated at the top of the stack

        capacity: [int] The maximum number of nodes that this stack can contain. 
        Not sure if this is standard, but I'm just putting it in to later implement 
        an is_full() method.
        """
        self.top = node
        self.capacity = capacity
        self.size = 1 if node else 0
    
    def push(self, value):
        """
        Parameters
        ----------
        value: [number or str] The value of the node to be added to the top of
        the stack.
        """
        if not self.is_full():
            # Make new node with value
            new_node = Node(value)

            # New node references the old top
            new_node.next = self.top

            # Put new node at top
            self.top = new_node

            self.size += 1
        
        else:
            raise SizeError('The stack is full so a value cannot be pushed')


    def pop(self):
        """
        Returns
        ------- 
        The top value from the stack. Also removes that node from the stack.
        """
        if self.is_empty():
            raise SizeError('Cannot pop from an empty stack.')
        else:
            old_top = self.top
            self.top = old_top.next
            self.size -= 1
            return old_top.value

    def peek(self):
        """
        Returns
        -------
        The value of the top node of the stack. If empty, returns None.
        """
        if self.is_empty():
            return None
        
        else:
            return self.top.value

    def is_empty(self):
        """
        Returns
        -------
        True if the stack has no nodes, False otherwise.
        """
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        Returns
        -------
        True if the stack's size is equal to the capacity
        """
        if self.size == self.capacity:
            return True
        else:
            return False

class SizeError(Exception):
    pass