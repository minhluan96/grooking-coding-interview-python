from utils.linked_list_node import LinkedListNode
from utils.linked_list import LinkedList
from utils.print_list import print_list_with_forward_arrow

def remove_duplicates(head):
    
    current = head

    while current:
        current_next = current.next

        if current_next and current.data == current_next.data:
            temp = current_next.next
            current.next = temp
            current_next.next = None
        else:
            current = current.next

    return head

arr = [-21,-21,-21,-21,-21,-21,-21]
linked_list = LinkedList()
linked_list.create_linked_list(arr)

result = remove_duplicates(linked_list.head)
print_list_with_forward_arrow(result)
