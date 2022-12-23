#           QUESTION 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

# def hello_name(user_name):
#     print(f'hello_{user_name}!')

# hello_name('USERNAME')


#           QUESTION 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

# def first_odds(num1, num2):
#     if num1>num2:
#         return
#     print(num1+2, end=" ")
#     return first_odds(num1+2,num2)
# num1=1;num2=100
# first_odds(num1,num2)


#           QUESTION 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

# def max_num_in_list(a_list):
#     max = a_list[0]
#     for a in a_list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1,3,9,0,18,36,]))


#              QUESTION 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

# def is_leap_year(a_year):
#     if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
#         return True
#     else:
#         return False 
# print(is_leap_year(1996)) 
#          
# 
# 
# 
#               QUESTION 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

# def is_consecutive(a_year):
#     return sorted(a_year) == list(range(min(a_year), max(a_year)+1))
    
# year = [3,2,8,6,5]
# print(is_consecutive(year))