'''
Implemntation of the Queue data stucture

07 October 2021
@author Bruce Mvubele
'''

class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def enque(self,data):
        new_node = Node(data)
        curr_node =self.top
        
        if curr_node is None:
            pass


if __name__ == '__main__':
    q=Queue()
    print(q)
    q.enque('a')
    q.enque('b')
    q.dequeue()
    print(q)