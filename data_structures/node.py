class Node:
    """
    The base class of a Node object for use in most of the data structures in 
    this directory. It is an object with no methods and only two attributes:

    value: [number or str]
    next: [Node or subclass] the node that this node references
    """
    def __init__(self, value):
        """
        Parameter
        ---------
        value: [number, str]
        """
        assert value != None, 'Don\'t make an empty-value node!'
        self.value = value
        self.next = None