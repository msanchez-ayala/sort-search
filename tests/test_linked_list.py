import pytest
from data_structures.linked_list import Node, DoublyLinkedNode, LinkedList

def get_llist(node_class):
    llist = LinkedList()
    llist.head = node_class(1)
    second = node_class(2)
    third = node_class(3)
    llist.head.next = second
    second.next = third

    if node_class == DoublyLinkedNode:
        second.prev = llist.head
        third.prev = second

    return llist


### SINGLY-LINKED NODES ###

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
        


    
class TestSinglyLinkedList:
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
    
    def test_singly_llist_push(self):
        llist = get_llist(Node)
        llist.push(0)
        assert isinstance(llist.head, Node), 'Pushed node is not of class Node'
        assert llist.head.value == 0, 'Pushed node has incorrect new value'

    def test_singly_llist_insert_after(self):
        llist = get_llist(Node)

        second = llist.head.next

        # Insert a new element after the second element
        llist.insert_after(second, 4)

        assert second.next.value == 4, 'Didn\'t insert at correct location'
        assert type(second.next) == Node, 'Inserted wrong class of Node'
    
    def test_singly_llist_append(self):
        llist = get_llist(Node)
        
        # Find last node for later testing
        last = llist.head
        while last.next:
            last = last.next
        
        llist.append(4)

        # last here is actually the previously last
        assert last.next.value == 4, 'New node not appended to end'
        assert type(last.next) == Node, 'New node is not of class Node'
    
    def test_singly_llist_remove_head(self):
        llist = get_llist(Node)
        llist.remove_head()
        assert llist.head.value == 2, 'Head wasn\'t removed'
        assert llist.head.next.value == 3, 'References weren\'t properly changed'
    
    def test_singly_llist_remove_node(self):
        llist = get_llist(Node)
        second = llist.head.next
        llist.remove_node(second)
        assert llist.head.value == 1, 'Head was modified'
        assert llist.head.next.value == 3, 'Node wasn\'t removed'
        
    def test_singly_llist_remove_last(self):
        llist = get_llist(Node)
        llist.remove_last()
        last = llist.head.next
        assert last.next == None, 'Last node remains'
        assert last.value == 2, 'More than just the last node was altered'


### DOUBLY-LINKED NODES ###
    
# class TestDoublyLinkedNode:
#     """
#     Cases not covered by Node's tests
#     """
#     def test_node_init(self):
#         node_1 = DoublyLinkedNode(1)
#         node_2 = DoublyLinkedNode(2)
#         node_1.next = node_2
#         node_2.prev = node_1 
#         assert node_2.prev == node_1

# class TestDoublyLinkedList:
#     def test_uniform_doubly_llist(self):
#         """
#         Make sure each element is of class DoublyLinkedNode and has a next() 
#         except for the last one.

#         Can check this by counting number of next pointers. Should be 1 less
#         than the total number ofnodes
#         """
#         # Maybe make a fixture
#         llist = get_llist(DoublyLinkedNode)
#         node = llist.head
#         next_count = 0
#         prev_count = 0

#         while node:
#             assert isinstance(node, DoublyLinkedNode)
#             if node.prev:
#                 prev_count += 1
#             if node.next:
#                 next_count += 1
#                 node = node.next
#             else:
#                 break
        
#         # No. of pointers = No. of nodes - 1
#         assert next_count == len(llist) - 1
#         assert prev_count == len(llist) - 1