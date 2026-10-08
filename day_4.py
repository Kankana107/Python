# 1. Match Case
# number = int (input("enter a number: "))
# match number:
#     case 1:
#         print("The number is 1")
#     case 2:
#         print("The number is 2")
#     case 3:
#         print("The number is 3")
#     case _:
#         print("No case matched")


# 2. Functions
# i) Without Arguements Without Return Value
# def my_function():
#     print("Hello World")
# my_function()

# ii) With Arguements Without Return Value
# def my_function(a):
#     print("Value is ",a)
# number = int(input("Enter a number: "))
# my_function(number)

# iii) Without Arguements With Return Value
# def my_function():
#     return("hello world")
# option 1
# print(my_function())
# option 2
# message = my_function()
# print(message)

# # iv) With Arguements With Return Value
# def my_function(a):
#     return(a)
#
# number = int(input("Enter a number: "))
# no = my_function(number)
# print("Value is: ", no)


# 3. Types of Arguments
# i) Positional Arguments
# def fun ( a,b,c):
#     return a+b-c
# print(fun(8,9,10))

# ii) Default Arguments
# def fun(a, c, b= 7):
#     return a+b-c
# # print (fun(5,8))
# print (fun(6,10,11))

# iii) Keyword Arguments
# def fun(a,b,c):
#     return a+b-c
# print(fun(a= 4, c= 2, b=8))

# iv) Arbitrary Arguments : Positional --- *args
# Case 1- in range
# def fun(*numbers):
#     for number in numbers:
#         print(number)
#
# number_list = []
# for i in range(5):
#     numbers = int(input("Enter a number: "))
#     number_list.append(numbers)
# fun(number_list)

# Case 2- for infinity numbers
# def fun(*numbers):
#     for number in numbers:
#         print(number)
#
# number_list = []
# while True:
#     numbers = (input("Enter a number: "))
#     if numbers == "exit":
#         break
#     number_list.append(int(numbers))
# fun(number_list)

# v) Arbitrary Arguments : Keyword --- **kwargs
# def fun(**numbers):
#     print("1st Number= ", numbers["x"])
#     print("2nd Number= ", numbers["y"])
#     print("3rd Number= ", numbers["z"])
# # fun(x=1, y=2, z=3)

# Using user input
# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))
# c= int(input("Enter the third number: "))
# fun(x=a, y=b, z=c)










