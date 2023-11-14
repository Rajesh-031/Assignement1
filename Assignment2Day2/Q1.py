#  define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

def add():
    print("Addition")
def modify():
    print("Modification")
def delete():
    print("Deletion")
choice = int(input("enter your choice : "))
match choice:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("invalid entry")