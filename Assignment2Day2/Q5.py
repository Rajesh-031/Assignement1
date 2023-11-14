# define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.

def myfun():
    num = int(input("Enter a number : "))
    if num>0:
        return 1
    elif num<0:
        return -1
    else:
        return 0
print(myfun())