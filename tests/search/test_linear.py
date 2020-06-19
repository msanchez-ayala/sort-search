import pytest
from search.linear import search_llist
from data_structures.linked_list import LinkedList
from data_structures.node import Node


def get_llist(node_class):
    llist = LinkedList()
    llist.head = node_class(1)
    second = node_class(2)
    third = node_class(3)
    llist.head.next = second
    second.next = third

    return llist

class TestSearchLList:

    def test_llist(self):
        llist = get_llist(Node)
        node = search_llist(llist, 2)
        assert node.value == 2, "Search didn't find element that was in llist"
        assert node.next.value == 3, "Node is not correctly linked"

        node = search_llist(llist, 4)
        assert node == None, "Search found an element that was not in llist"
