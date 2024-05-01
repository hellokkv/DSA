class Node:

    def __init__(self,value):
        self.value = value
        new_node =None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_list = LinkedList(10)
print(new_list.tail.value)