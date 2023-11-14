# 1) create a list , accept a number,name and a float value from user and store it inside the list.
# now accept one more name from user and insert it at 2nd position.
# accept a number and append it at the end of the list.
# print the entire list.

mylist = []
num = float(input("Enter a number : "))
name = input("enter a name : ")
height = float(input("enter your height : "))
mylist.append(num)
mylist.append(name)
mylist.append(height)
print(mylist)
new_name = input("Update the name : ")
mylist[1] = new_name
num1 = float(input("Enter a number : "))
mylist.append(num1)
print(mylist)