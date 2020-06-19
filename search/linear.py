def search_llist(llist, val):
    node = llist.head
    while node:
        if node.value == val:
            return node
        node = node.next
    return None
