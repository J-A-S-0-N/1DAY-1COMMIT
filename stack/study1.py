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
for  a in range(10):
    mystack.push(a)

print(mystack.stack_list)

for a in range(11):
    print(mystack.pop())