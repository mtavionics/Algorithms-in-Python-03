# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:01:15 2021
Project 3
@author: Mikhail Terentev

"""

class Empty(Exception):
    
    def __init__(self, message="Stack is empty"):
        self.message = message
        super().__init__(self.message)
    pass

class Full(Exception):

    def __init__(self, message="Stack is full"):
        self.message = message
        super().__init__(self.message)
    pass

class ArrayStack:
    '''LIFO Stack implementation using a Python list as underlying storage.
        new methods: 
            is_full(self)
            leacky_push - add elements to stack and if it's == maxlen then remove first one and add element to the end of stack
        changed:
            set maxlen in the __init__
            check if stack is full in push(self, e)
            pop(self, index) - added index to remove index elemnt from the stack;
    '''

    def __init__(self, maxlen=None):
        """Create an empty stack."""
        self._data = []      # nonpublic list instance
        self._maxlen=maxlen   # set maxlen in the __init__
        
    def __str__(self)   :
         """ Print stack length and members"""
         str_to_print = "Stack is empty" if self.is_empty() else "Stack array is: "
         str_to_print = "The lenght of Stack is {:2}. The maxlen={}. {}".format(self.__len__(),self._maxlen,str_to_print)
         return str_to_print + (','.join([str(element) for element in self._data]))
     
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)
    
    def is_full(self):
        """Return True if the stack is full."""
        if self._maxlen != None:
            return len(self._data) == self._maxlen   
        else:
            return False
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        if self.is_full( ):    # check if is full
             raise Full('Stack is full with {} elements when maxlen={}'.format(len(self._data),self._maxlen))   
        self._data.append(e) # new item stored at end of list
        return self._data[-1] 
    
    def leacky_push(self, e):
        """ Add element to the top of the stack. 
            If stack is full (has same number of elements as maxlen) remove first one"""
        if self.is_full( ):
            self.pop(0)
        self._data.append(e) # new item stored at end of list   
        return self._data[-1] 
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list
  
    def pop(self, index):   # add index
         """Remove and return the element from the "index" location.
         Raise Empty exception if the stack is empty.
         """
         if self.is_empty( ):
             raise Empty('Stack is empty')
         return self._data.pop(index) # remove last item from list   


def fillStack (N, n, ans = 'n'):
    ''' Fill the stack N with n number of members an is alpha or numeric '''
    for i in range(n):
        if ans == 'a':
            N.push(chr(97+i))
        elif ans == 's':
                N.push(chr(97+i))
                N.push(' ')
                i += 1
        else:
            N.push(i)   

def fillStack_leacky_push(N, n):
    ''' Fill the stack N with n number of numeric members '''
    for i in range(n):
        N.leacky_push(i)    


print ("----- Test using provided push() in Code Fragment 6.2 -----")
        
print("\n 1. Test when 'maxlen = None'")      
S = ArrayStack()
print(S)
fillStack(S, 7)
print(S)

print("\n 2. Test when 'maxlen = 0'. Exception 'Full' will risen at first push")      
try: 
    S = ArrayStack(0)
    print("Stack before testing:") 
    print(S)
    fillStack(S, 7)
    print("Stack after testing:") 
    print(S)
except Full as e:
    print("Exception 'Full' has risen: ", e.message )
    print(S)
    
print("\n 3. Test stack when maxlen=7. Exception 'Full' will risen at 8th push")   
try:    
    S = ArrayStack(7)
    print("Stack before testing:") 
    print(S)
    print("Create stack with 7 elements same as maxlen")
    fillStack(S, 7)
    print("Stack after creation:") 
    print(S)
    print("Add 8th element which is more than allowed by maxlen, expect exception")
    S.push(10)
except Full as e:
    print("Exception 'Full' has risen: ",e.message ) 
    print(S)

print("\n 4. Test add stack with maxlen=10. At 8th push first element will removed")   
try:    
    S = ArrayStack(7)
    print("Stack before testing:") 
    print(S)
    fillStack(S, 7,'n')
    print("Stack at full point:") 
    print(S)
    for i in range(3):
        S.leacky_push(10+i)
        print("Stack after added element {} even stack is full".format(10+i)) 
        print(S)
except Full as e:
    print("Exception 'Full' has risen: ", e.message )
    print(S)
    
 
print("\n----- Test using leacky_push() -----")

print("\n 1. Test when 'maxlen = None'")      
S = ArrayStack()
print(S)
fillStack_leacky_push(S, 7)
print(S)

print("\n 2. Test stack when 'maxlen = 0'. Exception 'Empty' will risen at first push")
try: 
    S = ArrayStack(0)
    print("Stack before testing:") 
    print(S)
    fillStack_leacky_push(S, 7)
    print("Stack after testing:") 
    print(S)
except Full as e:
    print("Exception 'Full' has risen: ", e.message )
    print(S)
except Empty as e:
    print("Exception 'Empty' has risen: ", e.message )
    print(S)    
    
print("\n 3. Test add stack when 'maxlen = 7'. At 8th push first element will removed")
try:    
    S = ArrayStack(7)
    print("Stack before testing:") 
    print(S)
    print("Create stack with 7 elements same as maxlen")
    fillStack_leacky_push(S, 7)
    print("Stack after creation:") 
    print(S)
    print("Add 8th element which is more than allowed by maxlen")
    S.leacky_push(10)
    print(S)
except Full as e:
    print("Exception 'Full' has risen: ", e.message ) 
    print(S) 
     
     
'''
Output:

----- Test using provided push() in Code Fragment 6.2 -----

 1. Test when 'maxlen = None'
The lenght of Stack is  0. The maxlen=None. Stack is empty
The lenght of Stack is  7. The maxlen=None. Stack array is: 0,1,2,3,4,5,6

 2. Test when 'maxlen = 0'. Exception 'Full' will risen at first push
Stack before testing:
The lenght of Stack is  0. The maxlen=0. Stack is empty
Exception 'Full' has risen:  Stack is full with 0 elements when maxlen=0
The lenght of Stack is  0. The maxlen=0. Stack is empty

 3. Test stack when maxlen=7. Exception 'Full' will risen at 8th push
Stack before testing:
The lenght of Stack is  0. The maxlen=7. Stack is empty
Create stack with 7 elements same as maxlen
Stack after creation:
The lenght of Stack is  7. The maxlen=7. Stack array is: 0,1,2,3,4,5,6
Add 8th element which is more than allowed by maxlen, expect exception
Exception 'Full' has risen:  Stack is full with 7 elements when maxlen=7
The lenght of Stack is  7. The maxlen=7. Stack array is: 0,1,2,3,4,5,6

 4. Test add stack with maxlen=10. At 8th push first element will removed
Stack before testing:
The lenght of Stack is  0. The maxlen=7. Stack is empty
Stack at full point:
The lenght of Stack is  7. The maxlen=7. Stack array is: 0,1,2,3,4,5,6
Stack after added element 10 even stack is full
The lenght of Stack is  7. The maxlen=7. Stack array is: 1,2,3,4,5,6,10
Stack after added element 11 even stack is full
The lenght of Stack is  7. The maxlen=7. Stack array is: 2,3,4,5,6,10,11
Stack after added element 12 even stack is full
The lenght of Stack is  7. The maxlen=7. Stack array is: 3,4,5,6,10,11,12

----- Test using leacky_push() -----

 1. Test when 'maxlen = None'
The lenght of Stack is  0. The maxlen=None. Stack is empty
The lenght of Stack is  7. The maxlen=None. Stack array is: 0,1,2,3,4,5,6

 2. Test stack when 'maxlen = 0'. Exception 'Empty' will risen at first push
Stack before testing:
The lenght of Stack is  0. The maxlen=0. Stack is empty
Exception 'Empty' has risen:  Stack is empty
The lenght of Stack is  0. The maxlen=0. Stack is empty

 3. Test add stack when 'maxlen = 7'. At 8th push first element will removed
Stack before testing:
The lenght of Stack is  0. The maxlen=7. Stack is empty
Create stack with 7 elements same as maxlen
Stack after creation:
The lenght of Stack is  7. The maxlen=7. Stack array is: 0,1,2,3,4,5,6
Add 8th element which is more than allowed by maxlen
The lenght of Stack is  7. The maxlen=7. Stack array is: 1,2,3,4,5,6,10

'''
        