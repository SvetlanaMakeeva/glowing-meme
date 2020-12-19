class ListContainer:

    def __init__ (self):
        self.my_list = [[None]*16, [None]*16]

    def my_add(self, index, index2, element):
        self.element = element
        self.index = index
        self.index2 = index2

        self.my_list[self.index][self.index2] = self.element

    def my_cout(self, index, index2):
        self.index = index
        self.index2 = index2
        print (self.my_list [self.index][self.index2])

    def showAll(self):
        print (self.my_list)


my_new_list = ListContainer()
my_new_list.my_add(1, 5, 10)
my_new_list.my_add(0, 5, "hello")
my_new_list.my_add(1, 6, "world")
my_new_list.showAll()
my_new_list.my_cout(0,5)
my_new_list.my_cout(1,6) 
