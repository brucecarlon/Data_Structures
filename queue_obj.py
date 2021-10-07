'''
Implemntation of the Queue data stucture

07 October 2021
@author Bruce Mvubele
'''


from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def is_empty(self):
        return len(self.data)==0

    def enque(self,item):
        self.data.append(item)

    def dequeue(self):
        return self.data.popleft()
    
    def size(self):
        return len(self.data)

    def peek(self):
        return self.data[0]
        
    def __str__(self) -> str:
        return str(self.data)

if __name__ == '__main__':
    q=Queue()
    print(q)
    q.enque('a')
    q.enque('b')
    q.dequeue()
    print(q)