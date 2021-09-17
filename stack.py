'''
Implemntation of the Stack data stucture

17 September 2021
@author Bruce Mvubele
'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if s.is_empty() == False:
            return self.items[-1]

    def get_stack(self):
        return self.items



if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    print(s.peek())