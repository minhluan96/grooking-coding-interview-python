from utils.linked_list import LinkedList
from utils.linked_list_node import LinkedListNode
from utils.swap_two_nodes import swap
from utils.print_list import print_list_with_forward_arrow
            
def swap_nodes(head, k):
    if not head or head.next is None:
        return head
    
    curr = head

    front, end = None, None
    count = 0

    while curr:
        count += 1
        
        if end is not None:
            end = end.next

        if count == k:
            front = curr
            end = head

        curr = curr.next

    swap(front, end)

    return head

arr = [4486,-1967,-679,-3641,-2688,-3366,755,-1974,2957,-2986,-4358,2487,3604,-513,621,819,295,-53,-1612,1995,315,4908,2194,-523,-1258,2216,-2223,-4114,-4322,3043,1492,-1405,-3563,3971,817,4981,-2989,-1888,-808,4887,1822,-4530,1531,4410,-1083,-4108,-2125,1699,-64,3253,-4723,-4202,-795,-1016,-1452,4291,2404,236,-110,-3397,-3275,3356,3196,-4306,782,876,-3409,4524,4627,-362,3892,2708,-1608,-1834,2239,-2355,3334,-361,4572,1338,-4532,1362,863,1760,-1343,-1671,-316,-2999,-2488,2666,4963,-1215,1411,-1135,1436,-2890,345,-3712,-1287,-4474,-347,3315,538,-3909]
k = 1
linked_list = LinkedList()
linked_list.create_linked_list(arr)
result = swap_nodes(linked_list.head, k)
print_list_with_forward_arrow(result)
