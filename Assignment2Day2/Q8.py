# write a function to accept minimum 3 characters and maximum 5 characters. 
#  	[ use default arguments method ]
def input_fun(char1,char2,char3,char4 ='A',char5 ='B'):
    return char1,char2,char3,char4,char5

char1 = input("Enter the First Character")
char2 = input("Enter the second character")
char3 = input("Enter the third character")
print(input_fun(char1,char2,char3,'C','D'))