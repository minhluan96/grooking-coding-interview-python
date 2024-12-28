from utils.linked_list import LinkedList
from utils.linked_list_reversal import reverse_linked_list


def palindrome(head):
    slow = fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    reverse_slow = reverse_linked_list(slow)

    while reverse_slow != None:
        if reverse_slow.data != head.data:
            return False

        reverse_slow = reverse_slow.next
        head = head.next

    return True


# arr = [1,2,3,2,1]
arr = [4,7,9,5,4]
a = LinkedList()
a.create_linked_list(arr)
head = a.get_head()
print(palindrome(head))