# 4) accept a number,string,decimal,boolean value and a character from the user
# and store it inside the list. First print the list from the beginning and then from the end.

mylist = []
roll_no = int(input("Enter the roll number : "))
name = input("Enter the name of the student : ")
marks = float(input("Enter Marks : "))
Pass = bool(input("Enter True if pass other wise False : "))

mylist.append(roll_no)
mylist.append(name)
mylist.append(marks)
mylist.append(Pass)

print(mylist)
print(mylist[::-1])





