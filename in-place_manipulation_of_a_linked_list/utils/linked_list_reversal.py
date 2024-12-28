# Template for reversing a linked list

def reverse_linked_list(head):
	prev, curr = None, head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev

def reverse_link_list_with_k(head, k):
	previous, current, next = None, head, None
	
	for _ in range(k):
		next = current.next
		current.next = previous
		previous = current
		current = next
		
	return previous, current

def reverse_linked_list_in_range(head, left, right):
	previous, current, next = None, head, None

	for _ in range(left, right):
		next = current.next
		current.next = previous
		previous = current
		current = next
	
	return previous, current