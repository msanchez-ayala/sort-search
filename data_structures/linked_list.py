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
        assert value, 'Don\'t make an empty-value node'
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
    
    def push(self, node):
        """
        Time complexity O(1) since we don't need to search.
        """
        old_head = self.head
        self.head = node

        if isinstance(node, DoublyLinkedNode):
            old_head.prev = self.head

        self.head.next = old_head

    
    # def insert_after(self, prev_node, new_node):
    #     assert prev_node, "prev_node must be a type of Node object"

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


def get_llist(node_class):
    llist = LinkedList()
    llist.head = node_class('first')
    second = node_class('second')
    third = node_class('third')
    llist.head.next = second
    second.next = third

    if node_class == DoublyLinkedNode:
        second.prev = llist.head
        third.prev = second

    return llist


if __name__ == '__main__':
    test_singly_llist()
    test_doubly_llist()
    test_append_start()