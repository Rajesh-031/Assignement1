# 3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] 
# at the end of the list using "extend" method.
mylist = []
i= 1
while(i<=5):
    element = int(input("Enter a number : "))
    mylist.append(element)
    i+=1
print("list before adding hardcoded values : ",mylist)
print("list after adding hardcoded values")
mylist.extend([10,20,30])
print(mylist)
    