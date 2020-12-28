class Node:

    def __init__(self, data):

        self.item = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):

        self.start_node = self.end_node = None

    def my_add(self, data):

        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def traverse_list(self):

        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")

                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):

        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = self.end_node = None
            return
        self.end_node.next = None
        self.end_node = None
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

new_linked_list = DoublyLinkedList()
new_linked_list.my_add(50)
new_linked_list.traverse_list()
