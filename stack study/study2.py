#todo
#make top function
#print the top obj if the stack is empty return -1
#make empty function
#if the stack is empty return 1 else return 0
#make size function
#print the size of the stack#

class stack:
    #this runs every time the class stack get called
    def __init__(self):
        #creating the list
        self.stack_list = []

    def push(self, data):
        #this line insert the data variable to the 0th pos 
        self.stack_list.insert(0, data)

    def pop(self):
        #if the stack_list is empty then return -1
        if self.stack_list == []:
            return -1
        #otherwise save res as -0th pos 
        else:
            res = self.stack_list[-0]
            del self.stack_list[-0]
            return res

    def top(self):
        #if the stack list is empty return -1 else return 0th pos 
        if self.stack_list == []:
            return -1
        else:
            return self.stack_list[0]

    def empty(self):
        #if the list is empty then return 1 otherwise return 0
        if self.stack_list == []:
            return 1
        else:
            return 0

    def size(self):
        #this return length of the list
        return len(self.stack_list)

#calling the stack list 
mystack = stack()

mystack.push(1)
mystack.push(2)
print(mystack.top())
print(mystack.size())
print(mystack.empty())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.size())
print(mystack.empty())
print(mystack.pop())
mystack.push(3)
print(mystack.empty())
print(mystack.top())