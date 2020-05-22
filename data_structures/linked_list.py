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
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
        
    def __repr__(self):
        """
        For shits and giggles
        """
        if not isinstance(self.head, DoublyLinkedNode):
            joiner = ' -> '
        elif isinstance(self.head, DoublyLinkedNode):
            joiner = ' <-> '

        string = str(self.head.value)
        node = self.head.next
        while node:
            string = joiner.join([string, str(node.value)])
            node = node.next
            
        return 'LinkedList {}'.format(string)
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


def prove_singly_llist():
    """
    Example to prove it's a properly functioning singly-linked list. 
    """
    llist = LinkedList()
    llist.head = Node('first')
    second = Node('second')
    third = Node('third')

    llist.head.next = second
    second.next = third

    llist.print_list()
    # print(len(llist))
    # print(repr(llist))

def prove_doubly_llist():
    """
    Now with doubly linked list
    """
    llist = LinkedList()
    llist.head = DoublyLinkedNode('first')
    second = DoublyLinkedNode('second')
    third = DoublyLinkedNode('third')

    llist.head.next = second
    second.prev = llist.head
    second.next = third
    third.prev = second

    print(repr(llist))

if __name__ == '__main__':
    prove_doubly_llist()