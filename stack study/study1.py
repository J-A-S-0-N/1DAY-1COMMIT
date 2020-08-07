# class Stack:
#     def __init__(self):
#         self.stack_list = []
    
#     def push(self,data):
#         self.stack_list.append(data)
    
#     def pop(self):
#         if self.stack_list == []:
#             return False
#         else:
#             res = self.stack_list[-1]
#             del self.stack_list[-1]
#             return res

# myStack = Stack()

# for a in range(10):
#     myStack.push(a)

# print(myStack.stack_list)

# for a in range(11):
#     print(myStack.pop())
    


# class stack:
#     def __init__(self):
#         self.stack_list = []

#     def push(self, data):
#         self.stack_list.append(data)

#     def pop(self):
#         if self.stack_list == []:
#             return False
#         else:
#             res = self.stack_list[-1]
#             del self.stack_list[-1]
#             return res

# myStack = stack()

# for a in range(10):
#     myStack.push(a)

# print(myStack.stack_list)

# for a in range(11):
#     print(myStack.pop())

class stack:
    def __init__(self):
        self.stack_list = []
    def push(self, data):
        self.stack_list.append(data)
    def pop(self):
        if self.stack_list == []:
            return False
        else:
            res = self.stack_list[-1]
            del self.stack_list[-1]
            return res

mystack = stack()
for a in range(10):
    mystack.push(a)

print(mystack.stack_list)

for a in range(11):
    print(mystack.pop())


#create class named stack
# def the init which will start whenever the mystack = stack() starts
# create an emtpy list in the init
# def push which will have "data" which will append to the list
# def pop it will pop or delete an object
# inside the def there is an if statement which if the list is empty return false
# else assign "res" to -1th postion of the list
# and delete the -1th pos
# the return the "res"#

#take out the class using mystack = stack()
# for a in range(10) 
# push a inside the list created in previous section
# print the list
# for a in range(11)
# pop and print at the same time#

class stack:
    def __init__(self):
        self.stack_list = []
    def push(self, data):
        self.stack_list.append(data)
    def pop(self):
        if self.stack_list == []:
            return False
        else:
            res = self.stack_list[-1]
            del self.stack_list[-1]
            return res

mystack = stack()
for a in range(10):
    mystack.push(a)

print(mystack.stack_list)

for a in range(11):
    print(mystack.pop())