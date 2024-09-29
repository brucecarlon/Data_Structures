'''
Implemntation of the Stack data stucture

17 September 2021
@author Bruce Mvubele
'''

class Node:
    def __init__(self,data = None,next=None) -> None:
        self.data = data
        self.next = next



class Stack():
    def __init__(self):
        self.top = None
        self.length = 0

    def get_stack(self)-> str:
        '''
        Returns stack as a string
        ------------------------
        
        '''
        stack_ = ''
        temp_node = self.top
        while temp_node:
            stack_ += str(temp_node.data) +'-->'
            temp_node = temp_node.next
        print(stack_)
        return stack_

    def push(self,data):
        '''
        Adds Node with data to the stack
        -------------------------------
        returns:
        None
        '''
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.length += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1
        return

    def pop(self):
        '''
        Removes and returns item at top of stock
        --------------------------------------
        Returns:
        Top node
        '''
        curr_node = self.top
        if curr_node is None:
            print('Stack is empty')
            return 'Stack is empty'
        else:
            self.top = curr_node.next
        return curr_node

    def is_empty(self):
        '''
        Checks if stack is empty
        ------------------------
        Returns:
        bool value
        '''
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        '''
        View the item at the top of the Stack

        --------------------------
        Returns:
        Top element of Stack
        '''
        if s.is_empty() == False:
            print(self.top.data)
            return self.top.data

        else:
            print('Stack is empty')

if __name__ == '__main__':
    s = Stack()
    s.peek()
    print(s.is_empty())
    s.push(1)
    s.push('new')
    s.push('fresh')
    s.get_stack()
    print(s.length)
    s.pop()
    print(s.is_empty())
    s.get_stack()
    s.peek()

