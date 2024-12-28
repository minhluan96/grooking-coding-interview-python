from utils.linked_list import LinkedList


def detect_cycle(head):

    slow = head
    fast = head

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next 

        if slow == fast:
            return True


    return False


a = LinkedList()
a.create_linked_list([2,4,6,8,10])
head = a.get_head()
last_index = a.get_length(head)
last_node = a.get_node(head, last_index - 1)
last_node.next = head

print(detect_cycle(head))