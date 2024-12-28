from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
            
def reverse(head):

    prev, next = None, None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    head = prev
    
    return head


arr = [1,-2,3,4,-5,4,3,-2,1]
a = LinkedList()
a.create_linked_list(arr)
head = a.get_head()
result = reverse(head)
print(str(a))