#2.i) Print all even numbers between 0 to 30 using for loop
# for i in range(1, 31):
#     if i % 2 == 0:
#       print(i)

#ii) Print all even numbers between 0 to 30 using while loop
# i = 0
# while i < 31:
#     print(i)
#     i = i + 1


#3.i) Print all odd numbers between 0 to 30 using for loop
# for i in range(1, 31):
#     if i % 2 != 0:
#         print(i)

# ii) Print all odd numbers between 0 to 30 using while loop
# i = 0
# while i < 31:
#     if(i % 2 != 0):
#         print(i)
#     i = i + 1


#3.i)Using continue using for loop
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

#ii)Using continue using while loop
# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


#4.i) Using break using for loop
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

#ii)Using break using while loop
# i = 0
# while i < 6:
#     i += 1
#     if i == 4:
#         break
#     print(i)


#5.Combination of user input,function,conditional statement,loop
#Take one user input to print even numbers using function
def user_fun(range_value):
    for i in range(range_value):
        if i % 2== 0:
            print(i)

n = int(input("Enter the range: "))
user_fun(n)