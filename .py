class Node:

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):

        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def delete_at_start(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return self.head

    def first(self):
        return self.head.data

    def printstack(self):

        print("stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

my_new_list = DoublyLinkedList()
my_new_list.push(7)
my_new_list.push(8)
my_new_list.push(9)
value = my_new_list.first()
print(value) 
my_new_list.delete_at_start()
my_new_list.printstack()
