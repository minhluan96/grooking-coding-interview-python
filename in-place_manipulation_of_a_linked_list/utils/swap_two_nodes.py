# Template for swapping two nodes of the linked list

def swap(node1, node2):
    temp = node1.data
    node1.data = node2.data
    node2.data = temp