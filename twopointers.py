# Two pointers moving in parrell
# For example -> Given a linked list with the following elements: 1 -> 2 -> 3 -> 4 -> 5, return to the 2nd to last element (4). In order to do this, you'll need some way of knowing how far away the 2nd to last element is from the end of the list. You can use two pointers to solve this problem.
# Time Complexity: O(n) -> space being allocated
import linkedlist
import node

def list_nth_last(linked_list, n):
    linked_list_as_list = []
    current_node = linked_list.head_node
    while current_node:
        linked_list_as_list.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return linked_list_as_list[len(linked_list_as_list) - n]

# pseudocode for this apporach because I am really confused
# nth last pointer = none
# tail pointer = linked list head node
# count = 1
# while tail pointer does exist
#    move tail pointer to the next node
#    increment count
#
#    if count > n + 1
#       if nth last pointer = none
#       set nth last pointer to head
#    else
#       move nth last pointer to the next node
# return nth last pointer
def nth_last_node(linked_list, n):
    current_node = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count > n + 1:
            if current_node is None:
                current_node = linked_list.head_node
            else:
                current_node = current_node.get_next_node()
    return current_node

# Pointers moving at different speeds
# For Example -> given the linked list with the following elements 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7, the middle node is 4. In order to find the middle node, you can use two pointers that move at different speeds.
# pseudocode for this approach
# create list
# while the linked list has not been fully iterated through
#   push the current element onto list
#   move foward one node
# return list[length/2]

# instead, we can use the two pointers to move through the linked list
# fast_pointer = linked list head node
# slow_pointer = linked list head node
# while fast pointer is not None:
    # move faster pointer to the next node
    # if the end of the linked list has been reached:
        # move fast pointer to the next node
        # move slow pointer to the next node
# return slow pointer
def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow
