# 1) write a function to accept a number and return its square using
# 	a) normal function
# 	b) lambda
"""
# method 1
def sqr(num):
    return num*num
num = int(input("enter a number"))
print(sqr(num))

# method 2
num = int(input("enter a number"))
sqr = (lambda num : print(num*num)) (num)
# lambda num : print(num*num) ==> takes the argument : and return its result which sqare of num
# (lambda num : print(num*num))(num) ==> immediately invokes the lambda function with the value num """

# 2) write a function to display "Hello World" using
# 	a) normal function
# 	b) lambda
"""
# method1
def mes():
    return "hello world"
print(mes())


# method2
mess = lambda : print("hello world")
mess() """

# 3) write a function with 2 arguments , second argument should be "default argument" and display them. Using
# 	a) normal function 
# 	b) lambda

#method1
"""
def fun (*arg1,arg2=10):
    return arg1,arg2
print(fun(10))
print(fun("rajesh"))

# # method2
fun = lambda x,y=10:  print("argument1:",x, "   argument 2:",y)
fun("rajesh")
fun(100) """

#4) write a function with variable no. of arguments and display them. Using
# 	# a) normal function
# def fun(*args):
#      return args
# print(fun(1,2,3,4,5,6,7))
"""
	# b) lambda
fun = (lambda *args:[print(i) for i in args])(1,2,3,4,5,6)

# method1
def func(**args):
    return args
print(func(name = "Rahul",age = 27,add = "Mumbai"))

# #method2
(lambda **args : [print(k,y) for k,y in args.items()])(name="rahul",age=27)
"""





