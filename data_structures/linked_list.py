"""
A linked list is a linear collection of data elements, whose order is not
given by their physical placement in memeory. Instead, each element POINTS to
the next. It's a data structure consisting of a collection of nodes which
together represent a sequence.

Each node contains data and a reference to the next node in the sequence.

Advantages: 
-- Efficient insertion or removal of elements from any position during iteration.
-- Easy insertion or removal without reallocation of the entire structure.

Drawbacks:
-- Access time is linear. Arrays have better cache locality than these.


(value, pointer) = Node

Singly Linked List Example
---------------------------

(5, ->) (-2, ->) (8, ->) (X)

The last node is a terminator used to signify the end of the list.

Doubly Linked List Example
---------------------------

(X) (<- 5 ->) (<- -2 ->) (<- 8 ->) (X)
"""

class Node:
    """
    Parent class for nodes in linkedlist. subclasses will handle doubly linked
    relationships.
    """
    def __init__(self, value):
        """
        Parameter
        ---------
        value: [number, str]
        """
        assert value != None, 'Don\'t make an empty-value node'
        self.value = value
        self.next = None

class DoublyLinkedNode(Node):
    """
    Child class for doubly linked nodes
    """
    def __init__(self, value):
        """
        Parameter
        ---------
        value: [number, str]
        """
        super().__init__(value)
        self.prev = None
    
class LinkedList:
    def __init__(self, head = None):
        """
        Parameters
        ----------
        head: [Node or subclass of Node] The head node. Can be empty to start 
        off.
        """
        self.head = head
    
    def push(self, value):
        """
        Add a value to beginning of llist.
        Time complexity O(1) since we don't need to search.

        Parameters
        ----------
        value: [number or str] The value of the new node to be inserted.
        """
        old_head = self.head
        new_head = Node(value)
        self.head = new_head

        if isinstance(new_head, DoublyLinkedNode):
            old_head.prev = self.head

        self.head.next = old_head

    
    def insert_after(self, prev_node, new_value):
        """
        Add a new node after a previous node

        Parameters
        ----------
        prev_node: [Node or subclass] The node after which to add a new node.

        new_value: [number or str] The value of the new node to be inserted.
        """
        assert isinstance(prev_node, Node), "prev_node must be a type of Node object"

        # Instantiate
        new_node = Node(new_value)

        # Give the new node a next value
        new_node.next = prev_node.next

        # Make the new node the next of the previous node
        prev_node.next = new_node
    
    def append(self, new_value):
        """
        Adds a new node at the end of this llist.

        Parameters
        ----------
        new_value: [number or str] The value of the new node to be appended.
        """
        # Instantiate
        new_node = Node(new_value)

        # If this is an empty llist, we need to set the head
        if self.head == None:
            self.head = new_node
        
        # Otherwise, proceed as normal
        else:

            # Find the final node
            last = self.head
            while last.next:
                last = last.next
            
            # Add a new node after the final node
            last.next = new_node


    def print_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        

    def __repr__(self):
        """
        For a little clearer printing
        """
        if not isinstance(self.head, DoublyLinkedNode):
            joiner = ' -> '
            kind = 'Singly Linked List'
        elif isinstance(self.head, DoublyLinkedNode):
            joiner = ' <-> '
            kind = 'Doubly Linked List'

        string = str(self.head.value)
        node = self.head.next
        while node:
            string = joiner.join([string, str(node.value)])
            node = node.next
            
        return '{}: {}'.format(kind, string)
    
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


