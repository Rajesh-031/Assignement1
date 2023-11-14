# define a function which accepts a character and return toggle of it
def fun():
    char = input("Enter a character : ")
    chascii = ord(char)
    if chascii>=65 and chascii<=90:
        print("UPPERCASE")
    elif chascii>=97 and chascii<=122:
        print("lowercase")
    else:
        print("this is not a character")
fun()