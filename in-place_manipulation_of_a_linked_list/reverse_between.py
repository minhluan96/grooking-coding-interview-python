from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
from utils.linked_list_traversal import traverse_linked_list
from utils.linked_list_reversal import reverse_linked_list_in_range
from utils.print_list import print_list_with_forward_arrow


def reverse_between(head, left, right):

	if not head or left == right:
		return head

	dummy = LinkedListNode(0)
	dummy.next = head
	prev = dummy

	# traverse to the left node
	for _ in range(left - 1):
		prev = prev.next

	# prev is the previous of the curr
	# curr is the left node
	curr = prev.next

	print('before enter', curr.data)
	print('####')

	for _ in range(right - left):
		next_node = curr.next
		curr.next = next_node.next
		next_node.next = prev.next
		prev.next = next_node

		print('prev', str(prev.data), 'prev next', str(prev.next.data))
		print('curr', str(curr.data), 'curr next', str(curr.next.data))
		print('next', str(next_node.data), 'next next', str(next_node.next.data))
		print('###')

	return dummy.next
		

	

arr = [-499,399,-299,199,-99,9] 
# after 1st iteration
# [-499,399,199,-299,-99,9]
left = 3
right = 5

linked_list_arr = LinkedList()
linked_list_arr.create_linked_list(arr)

result = reverse_between(linked_list_arr.head, left, right)
print_list_with_forward_arrow(result)
