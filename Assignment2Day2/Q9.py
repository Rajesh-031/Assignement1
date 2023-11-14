# define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]
def sum_fun(*varg):
    sum = 0
    for val in varg:
        sum +=val
    return sum
print(sum_fun(10,20,30,40,50,60))
