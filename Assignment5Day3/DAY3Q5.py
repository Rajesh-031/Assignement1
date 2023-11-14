# 5) accept 5 numbers, store them inside the list. now accept a number from user which he would like
# to remove from the list and  after removing it, display the list.
mylist = []
for i in range(1,6):
    num = int(input("Enter a number : "))
    mylist.append(num)
print(mylist)
num1 = int(input("Enter a number to delete from list : "))
mylist.remove(num1)
print(mylist)
