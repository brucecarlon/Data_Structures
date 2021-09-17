# Create a singly linkedlist


class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    
class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        elem = []
        while cur_node != None:
            print(cur_node)
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)

        if self.head == None: # check if list is empty if it is append to the first index
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node =  last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node,data):
        if not prev_node:
            print('Previous node is not list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def delete_node(self,key):
        cur_node = self.head
        #delete a head node
        if cur_node and cur_node.data == key :
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node != None and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node == None:
            return
        prev.next = cur_node.next
        cur_node = None

llist = LinkedList()
llist.append('a')
llist.append('b')
llist.prepend('z')
llist.insert_after_node(llist.head.next,'e')
llist.delete_node('e')
llist.print_list()

