import pytest
from data_structures.linked_list import Node, DoublyLinkedNode, LinkedList, get_llist

class TestNode:
    def test_node_init(self):
        node_1 = Node(1)
        assert node_1.value == 1, 'Didn\'t init value correclty'
        assert node_1.next == None, 'Constructed a filled next value'

        node_2 = Node(2)
        node_1.next = node_2
        assert node_1.next == node_2, "Next assignment not working"

    def test_node_value_error(self):
        with pytest.raises(AssertionError):
            Node(None)
            Node('')
        

class TestDoublyLinkedNode:
    """
    Cases not covered by Node's tests
    """

    def test_node_init(self):
        node_1 = DoublyLinkedNode(1)
        node_2 = DoublyLinkedNode(2)
        node_1.next = node_2
        node_2.prev = node_1 
        assert node_2.prev == node_1
    
class TestLinkedList:
    def test_init(self):
        node_1 = Node(1)
        llist = LinkedList(node_1)
        assert llist.head == node_1, 'Didn\'t construct head correctly.'

    def test_uniform_singly_llist(self):
        """
        Make sure each element is of class Node and has a next() except for the 
        last one.

        Can check this by counting number of next pointers. Should be 1 less
        than the total number ofnodes
        """
        # Maybe make a fixture
        llist = get_llist(Node)
        node = llist.head
        count = 0

        while node:
            assert isinstance(node, Node)
            if node.next:
                count += 1
                node = node.next
            else:
                break
        
        # No. of pointers = No. of nodes - 1
        assert count == len(llist) - 1
    
    def test_uniform_doubly_llist(self):
        """
        Make sure each element is of class DoublyLinkedNode and has a next() 
        except for the last one.

        Can check this by counting number of next pointers. Should be 1 less
        than the total number ofnodes
        """
        # Maybe make a fixture
        llist = get_llist(DoublyLinkedNode)
        node = llist.head
        next_count = 0
        prev_count = 0

        while node:
            assert isinstance(node, DoublyLinkedNode)
            if node.prev:
                prev_count += 1
            if node.next:
                next_count += 1
                node = node.next
            else:
                break
        
        # No. of pointers = No. of nodes - 1
        assert next_count == len(llist) - 1
        assert prev_count == len(llist) - 1
    
