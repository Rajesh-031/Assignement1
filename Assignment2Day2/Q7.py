# define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]

def toggle_fun():
    str = input("Enter a string : ")
    toggled_str = str.swapcase()
    return toggled_str
print(toggle_fun())
    
    