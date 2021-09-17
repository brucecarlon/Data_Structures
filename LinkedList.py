# Create a singly linkedlist

elem = []

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    
class SLinkedList():
    '''Singly linked list'''
    def __init__(self):
        self.head = None
    def print_list(self):
        cur_node = self.head
        global elem
        while cur_node != None:
            print(cur_node)
            elem.append(cur_node)
            cur_node = cur_node.next

    def append(self,data):
        '''
        Inserts new element to end of list
        '''
        new_node = Node(data)
        if self.head == None: # check if list is empty if it is append to the first index
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node =  last_node.next
        last_node.next = new_node

    def prepend(self,data):
        '''
        Inserts new element to start of list
        '''
        new_node=Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node,data):
        '''
        Inserts element after a given node
        '''
        if not prev_node:
            print('Previous node is not list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
        '''
        Deletes node with a given data field from list
        '''
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

    def delete_node_at_pos(self,pos):
        ''' Deletes node at specified position'''
        cur_node = self.head
        
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        rev = None
        count = 1

        while cur_node != None and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count +=1
        if cur_node == None:
            return "Position is out of range"

        prev.next = cur_node.next
        cur_node = None


    def length(self):
        '''Finds length of linked list'''
        cur = self.head
        total = 0
        while cur != None:
            total += 1
            cur = cur.next
        return total

if __name__ == '__main__':
    llist = SLinkedList()
    llist.append('a')
    llist.append('b')
    llist.prepend('z')
    llist.prepend('k')
    llist.prepend('gamma')
    llist.insert_after_node(llist.head.next,'e')
    llist.delete_node('e')
    llist.delete_node_at_pos(0)
    llist.print_list()
    print(llist.length())
