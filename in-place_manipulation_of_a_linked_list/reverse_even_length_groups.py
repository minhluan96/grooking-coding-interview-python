from utils.linked_list import LinkedList
from utils.linked_list import LinkedListNode

def reverse_even_length_groups(head):
    # node immediately before the current group
    prev = head

    # The head doesn't need to be reversed since it's a group of one node,
    # so starts with length 2
    group_len = 2

    while prev.next:
        node = prev
        num_nodes = 0

        # traversing all the nodes of the current group
        for _ in range(group_len):
            if not node.next:
                break
            num_nodes += 1
            node = node.next
        
        # odd length
        if num_nodes % 2:
            prev = node
        else:
            #even length

            # reverse will be the next node of the current group
            reverse = node.next
            curr = prev.next

            for _ in range(num_nodes):
                curr_next = curr.next
                curr.next = reverse
                reverse = curr
                curr = curr_next
            
            # prev_next is the first node of the current group
            prev_next = prev.next
            prev.next = node
            prev = prev_next
        
        group_len += 1

    return head