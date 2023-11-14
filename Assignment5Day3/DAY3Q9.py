# 9) accept 5 names and store them in list. Now sort the list in ascending order display 
# and then in descending order.

mylist = []
for i in range(1,6):
    name = input("Enter a name : ")
    mylist.append(name)
    
print(mylist)
print(sorted(mylist))
print(sorted(mylist,reverse=True))
