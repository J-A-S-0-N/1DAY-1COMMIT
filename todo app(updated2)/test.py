import os

os.chdir("C:\\Users\\jason\\Desktop\\_\\coding\\python\\python\\else\\todo app")
file = open("todo.txt", "r+")

data_test = file.read()
print(data_test)
data_test_list = data_test.split(",")
for i in data_test_list:
    print(i)
