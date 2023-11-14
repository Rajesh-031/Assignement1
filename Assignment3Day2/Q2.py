# define nested function and show how will you invoke it.
def outer_fun():
    print("inside the outer function")
    def inner_fun():
        print("inside the inner function")
    return inner_fun

# call method 1
# var = outer_fun()
# var()

# call method 2
outer_fun()()
        
