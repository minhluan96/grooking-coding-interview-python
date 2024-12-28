from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode

def merge_2_lists(head1, head2):
    dummy = LinkedListNode(-1)
    prev = dummy

    # traverse over the lists until both or one of them becomes null
    while head1 and head2:
        if head1.data <= head2.data:
             # if l1 value is <=  l2 value, add l1 node to the list
            prev.next = head1
            head1 = head1.next
        else:
            # if l1 value is greater than l2 value, add l2 node to the list
            prev.next = head2
            head2 = head2.next

        prev = prev.next

    if head1 is not None:
        prev.next = head1
    else:
        prev.next = head2
    
    return dummy.next



def merge_k_lists(lists):
    if len(lists) > 0:
        step = 1
        while step < len(lists):
            # The loop merges lists that are 'step' apart.For example, if we have 4 lists (L1, L2, L3, L4), with step = 1, we'll first merge L1 with L2, and L3 with L4 etc,
            # After each iteration, the step size doubles (step *= 2). This merges the results of previous merges, 
            # For example, after the first iteration with step = 1, we merge the results of L1 + L2 with L3 + L4 in the next iteration when step = 2.
            
            for i in range(0, len(lists) - step, step * 2):
                lists[i].head = merge_2_lists(lists[i].head, lists[i + step].head)

            step *= 2
        
        return lists[0].head
    return
        