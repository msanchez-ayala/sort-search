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
from .node import Node

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
        node_type = type(self.head)
        old_head = self.head
        new_head = node_type(value)
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
    
    def remove_head(self):

        # Remove the head unless this linked list has only one element
        self.head = self.head.next if self.head.next else None
    
    def remove_node(self, node_to_remove):

        # Find the node right before the node to remove
        node = self.head
        while node:
            if node.next == node_to_remove:
                node.next = node_to_remove.next
                break
            node = node.next
            

    def remove_last(self):

        # Find second to last element
        last = self.head
        while last.next:
            second_last = last
            last = last.next
        
        # Remove reference to the last node in the list
        second_last.next = None
        



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


