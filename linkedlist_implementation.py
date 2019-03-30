# To create the new node.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# To perform the operation on the linked list.
class Linkedlist:
    def _init__(self):
        self.head = None
     
    # A function to print the linked list.
    def printlist(self):
        print("THE LINKED LIST IS :")
        printl = self.head
        while printl is not None:
            print(printl.data)
            printl = printl.next

    # A function to add a node at the beginning of the linked list.        
    def addbeg(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
        print(newdata,"is added at beginning")

    # A function to add a node at the end/last of the linked list.
    def addlast(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            print(newdata, "is added at end")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = NewNode
        print(newdata, "is added at end")
   
    # A function to add a node in between of the linked list.
    def mid(self, a, newdata):
        temp = self.head
        for i in range(1, a):
            if temp.next is None:
                print(a,"node is absent so the newdata can not be added")
                return
            temp = temp.next
        NewNode = Node(newdata)
        NewNode.next = temp.next
        temp.next = NewNode
        print(newdata, "is added at the",a,"position")

    # A function to delete/remove a node from the linked list.    
    def remove(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                print(key, "is deleted from the linked list")
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print(key, "is not present in the linked list. so, it can not be deleted")
            return
        prev.next = temp.next
        temp = None
        print(key, "is deleted from the linked list")


l = Linkedlist()
l.head = Node("1")
l1 = Node("2")
l2 = Node("3")
l.head.next = l1
l1.next = l2
l.addbeg("0")
l.addlast("5")
l.mid(4, "4")
l.mid(8, "6")
l.addlast("6")
l.printlist()
l.remove("6")
l.remove("7")
l.printlist()
