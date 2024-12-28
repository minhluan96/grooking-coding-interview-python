import math
from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
from utils.linked_list_traversal import traverse_linked_list
from utils.linked_list_reversal import reverse_link_list_with_k
            
def reverse_k_groups(head, k):
  
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy

    while ptr is not None:
        tracker = ptr

        for i in range(k):
            if tracker == None:
                break

            tracker = tracker.next

        if tracker == None:
            break
        
        previous, current = reverse_link_list_with_k(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group


    return dummy.next