# create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
# invoke caller function by passing show1,show2 and show3

def caller(fun):
    fun()

def show1():
    print("inside show1")
def show2():
    print("inside show2")
def show3():
    print("inside show3")

caller(show1)
caller(show2)
caller(show3)