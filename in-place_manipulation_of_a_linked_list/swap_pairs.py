from utils.linked_list import LinkedList
from utils.print_list import print_list_with_forward_arrow

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    current = head
    while current and current.next:
        current_next = current.next
        
        temp = current.data
        current.data = current_next.data
        current_next.data = temp

        current = current_next.next

    return head

arr = [1,2,3,4]
linked_list = LinkedList()
linked_list.create_linked_list(arr)
result = swap_pairs(linked_list.head)
print_list_with_forward_arrow(result)


'''
 a, b

 temp = a
 a = b
 b = temp

 current, current_next
 temp = current
 current = current_next
 current_next = current
'''