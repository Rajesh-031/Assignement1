# 6) accept 5 numbers, store them inside the list. now accept a position from user ,
# remove the element from that position and  after removing it, display the list.

mylist = []
for i in range(1,6):
    element = int(input("Enter the element : "))
    mylist.append(element)
print(mylist)
print("Number of elements : ",len(mylist))

pos = int(input("Enter the position of element to delete the number : "))
mylist.pop(pos-1)
print(mylist)