'''
Implemntation of the Stack data stucture

17 September 2021
@author Bruce Mvubele
'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        ''' 
        Appends item to top of stack

        PARAMETER:
        Item to append to stack

        ---------------------

        Returns:
        Stack with appended item
        '''
        self.items.append(item)

    def pop(self):
        '''
        Removes and returns item at top of stock

        '''
        return self.items.pop()

    def is_empty(self):
        '''
        Checks if stack is empty
        ------------------------
        Returns:
        bool value
        '''
        return self.items == []

    def peek(self):
        '''
        View the item at the top of the Stack

        --------------------------
        Returns:
        Top element of Stack
        '''
        if s.is_empty() == True:
            return self.items[-1]

        else:
            print('Stack is empty')

    def get_stack(self):
        '''
        Returns:
        Stack
        '''
        return self.items



if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    #print(s.peek())
    #print(s.get_stack())

    c = Stack()
    print(c.is_empty())
    print(c.get_stack())
    c.peek()
