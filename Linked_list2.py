
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

#--------------------SEARCH ITEM FROM LL-----------------

    def search(self, search_data):
        n = self.head.next

        while n != None:
            if n.data == search_data:   #self.head.next.data == search_data
                print("\n\nData found in linked list.")
                return

            n = n.next  # traverse: self.head.next = self.head.next.next
        print("\n\nData not found")   # if data not found


ll = LinkedList()
print("\nAdded elements at begining : ")
ll.add_end(20)
ll.add_end(30)
ll.add_end(40)
ll.add_end(50)
ll.add_end(60)
ll.add_end(70)
ll.print_LL()

ll.search(70)
ll.search(170)











