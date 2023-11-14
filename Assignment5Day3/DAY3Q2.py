# 2) first create list empty. accept numbers till user enters 0 and store them inside the list.
# Print the list and its length.


mylist = []
while(1):
    num = int(input("enter a number : "))
    if num == 0:
        break
    else:
        mylist.append(num)
print(mylist)
print("Number of elements in the list are : ",len(mylist))