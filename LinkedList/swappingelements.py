# Given a linked list and the elements to be swapped (val1 and val2), we need to keep track of four values:
# node1, node1_prev, node2, node2_prev. We need to swap the nodes and update the pointers accordingly.

import node
import linkedlist

def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}\n')

    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    while node2 is not None:
         if node2.get_value() == val2:
             break
         node2_prev = node2
         node2 = node2.get_next_node()
    # updating preceding nodes
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)
    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)
    # updating the nodes next pointers
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
    # Edge Cases - What if there is no matching niode for one of the inputs? The current swap_nodes() functions will not run out because we will try to access the next node of a node that is None. Here is the fix.
    if node1 is None or node2 is None:
        print("Swap not possible - one or more element is not in the list")
        return
    if val1 == val2:
        print("Swap not possible - elements are the same")
        return
    # displaying the list with swapped_nodes being used
    ll = linkedlist.LinkedList()
    for i in range(10):
        ll.append(i)

    print(ll.stringify_list())
    swap_nodes(ll, 1, 2)
    print(ll.stringify_list())
