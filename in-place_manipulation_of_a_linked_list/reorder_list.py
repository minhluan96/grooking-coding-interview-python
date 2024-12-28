from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
from utils.print_list import print_list_with_forward_arrow
            
def reorder_list(head):
    if not head:
        return head
    
    slow = fast = head

    # find the middle of linked list
    # in 1->2->3->4->5->6 find 4 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second part of the list
    # convert 1->2->3->4->5->6 into 1->2->3 and 6->5->4
    # reverse the second half in-place
    prev, curr = None, slow

    while curr:
        # using inline assignment to avoid using temp variable
        curr.next, prev, curr = prev, curr, curr.next

    # merge two sorted linked lists
    # merge 1->2->3 and 6->5->4 into 1->6->2->5->3->4
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head


arr = [1,1,2,2,3,-1,10,12]

'''
    reverse mid = 12 -> 10 -> -1 -> 3

    mid node = 12
    
    first node = 1
    next first = 1
    next mid = 10

    first node.next = 1 -> 12
    next mid = next mid.next = 10
    first node = first node.next = 12

'''

linked_list = LinkedList()
linked_list.create_linked_list(arr)
result = reorder_list(linked_list.head)

print_list_with_forward_arrow(result)