import node
class LinkedList:
    def __init__(self):
        self.head_node = None
    def get_head_node(self):
        return self.head_node
    def insert_beginning(self, new_value):
        new_node = node.Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def append(self, value):
        new_node = node.Node(value)
        current_node = self.get_head_node()
        if not self.head_node:
            self.head_node = new_node
            return
        current_node = self.head_node
        while current_node.get_next_node():
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def remove_node(self, node_to_remove): #removing the middle node of a linked list
        current_node = self.get_head_node()
        if current_node.get_value() == node_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == node_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def display(self):
        nodes = []
        current_node = self.head_node
        while current_node:
            nodes.append(current_node.get_value())
            current_node = current_node.get_next_node()
        print(" -> ".join(map(str,nodes)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print("Original Linked List:")
ll.display()

ll.remove_node(3)
print("Linked List after removing the middle node: ")
ll.display()
