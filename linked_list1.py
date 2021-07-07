
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def get_length(self):
        count = 0
        n = self.head
        while n:
            count = count + 1
            n = n.next
        return count


    def print_LL(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.next

    def add_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  # new node becomes new head


    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node #n.next is None
            
#--------------------REMOVE ITEM FROM LL-----------------

    def remove(self, x):
        if self.head is None:
            print("Can't delete because LL is empty.")
            return

        # removing 1st item
        if x == self.head.data:
            self.head = self.head.next
            return

        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next

        if n.next is None:
            print("Node is not present")
        else:
            n.next = n.next.next



ll = LinkedList()
print("\nAdded elements at begining : ")
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)
ll.add_end(50)
ll.add_end(60)
ll.add_end(70)
ll.print_LL()



print("\nAfter removing element: ")
ll.remove(30)
ll.print_LL()











