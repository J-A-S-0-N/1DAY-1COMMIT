class stack:
    def __init__(self):
        self.stack_list = []
    
    def push(self, data):
        self.stack_list.insert(0,data)

    def pop(self):
        if self.stack_list == []:
            return -1
        else:
            res = self.stack_list[-1]
            del self.stack_list[-1]
            return res

    def size(self):
        return len(self.stack_list)

    def top(self):
        if self.stack_list == []:
            return -1
        else:
            return  self.stack_list[0]

    def empty(self):
        if self.stack_list == []:
            return 1
        else:
            return 0

my_stack = stack()


#stuff to remember
# in push you need to insert rather than append because if you append it will append at the end of the list
# 
# everything needed to return -1 if the list is empty exept init push and size
# 
# in top just return the 0th pos of the list#