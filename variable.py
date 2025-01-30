# letter = ''' dear <|name|>
# you are selected!
# <|DATE|>'''
# print(letter.replace("<|name|>","saurabh").replace("<|DATE|>","28 september"))

#########################################
#############################################
# str = '   saurabh'
# new_str = str.lstrip
# print(new_str)
######################################
#######################################
# fruit = []
# count = 0
# # for i in range(1,8):
# #     print(fruit.append(f1))

# while count<8:
#     f1 = input("enter fruit name :")
#     fruit.append(f1)
#     count += 1
# print(fruit)
############################
###############
# list_of_marks = []
# count=0
# while count<6:                                     #doubt 
#     list = [input("enter marks here: ")]
#     list_of_marks.append(list)
#     count+=1
# print(list_of_marks)
############################################
# ##############################################
# a = (3,4,0,0,4,0)
# n = a.count(0)
# print(n)
##################################
##################################
# dict = { "kurshi":"chair","kalam":"pen","kitab":"book"}
# word = input("enter the word ")
# print(dict[word])
# #################################################
####################################################
# s = set()
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# n = int(input("enter a number: "))
# s.add(n)
# print(s)
###################################
####################################
# s = set()
# count = 0
# while count<6:
#     n= int(input("enter a number: "))
#     s.add(n)
#     count+=1
# print(s)
####################################
#######################33333333333
# s =set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))
##############################
##########################
# s={}
# print(type(s))
###############################
#####################
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# num4 = int(input("enter a number: "))
# if num1>num2 and num2>num3 and num3>num4:
#     print("num1 is greater :-",num1)
# elif  num2>num1 and num2>num3 and num3>num4:
#     print("num2 is greater :-",num2)
# elif num3>num1 and num3>num2 and num3>num4:
#     print("num3 is greater :-",num3)
# else:
#     print("num4 is greater:-",num4)
    
#############################################
#############################################
# marks1 = int(input("enter the marks: "))
# marks2 = int(input("enter the marks: "))
# marks3 = int(input("enter the marks: "))
# marks_percentage = 100*(marks1+marks2+marks3)/100
# if marks_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33:
#     print(f"congratulation you passed the exam ",{marks_percentage})
# else:
#     print("try next time")
##########################################
#############################################
# spam1 = "make a lot of money"
# spam2 = "buy now"
# spam3 = "subscribe this"
# spam4="click this"
# str1 = input("enter  sentences ")
# if spam1 or spam2 or spam3 or spam4 in str1:
#     print("this is spam alert")
# else:
#     print("this is not spam")
######################################
############################################
# name = input("enter a string:- ")
# if (len(name)<10):
#     print("please enter username greater than 10 character")
# else:
#     print("go to the next page")
##################################################
##################################################
# num = int(input("enter a number:-"))
# for i in range(1,11):
#     print(num*i)
##################################################
#######################################################
# list1 = ['harry','saurabh','sachin',"rohan"]
# for name in list1:
#     if (name.startswith("s")):
#         print(f"good morning,{name}")
###########################################
#################################################
# num = int(input("enter a number: "))
# count = 1
# while count<=10:
#     print(num*count)
#     count+=1
######################################################
#########################################################
# num= int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num}*{11-i}={num*(11-i)}")
###########################################################
############################################################
# Basic Questions
# Write a function add_numbers(a, b) that takes two numbers as arguments and returns their sum.
# def add(a,b):
#     print(f"sum of a and b is :{a+b}")
# add(8,9)
######################################################
#####################################################

# Create a function is_even(n) that checks whether a number is even or odd. Return True if even, otherwise False.
# def check_even_odd(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# print(check_even_odd(8)) 
#########################################################################################################
###########################################################################################################

# Write a function greet(name) that takes a name as input and prints a personalized greeting, e.g., "Hello, [Name]!".
# def greet():
#     print(f"hello{name}")
# greet(name)

# name = input("Enter the name: ")

# def greet(name):
#     print(f"Hello, {name}!")  
# greet(name)  

# Create a function find_max(a, b, c) that takes three numbers and returns the largest of them.
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# def find_max(a,b,c):
#     print(f"maximum value in given three number: ",max(a,b,c))
# find_max(num1,num2,num3)
# # Write a function factorial(n) to calculate the factorial of a given number using a loop.
# n=int(input("enter a number:"))
# factorial= 1
# for i in range(1,n+1):
#     factorial *=i
#     print(f"factorial of {n} is {factorial}")
#######################################################################
# n = int(input("Enter a number: "))

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     print(f"Factorial of {n} is {result}")

# factorial(n)

    
##############################
##############################
# Intermediate Questions
# Write a function fibonacci(n) that generates the first n terms of the Fibonacci series.

# Create a function is_palindrome(s) that checks if a given string s is a palindrome.
# def is_palindrome(s):
    
#     return s == s[::-1]


# s = input("Enter a string: ")
# if is_palindrome(s):
#     print(f"{s} is a palindrome.")
# else:
#     print(f'"{s}" is not a palindrome.')


# Write a function prime_numbers(limit) that prints all prime numbers up to a given limit.
# num = int(input("enter a number: "))
# def check_prime(num):
#     # Initially assume the number is prime
#     is_prime = True

#     # Check divisibility from 2 to the square root of num
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
    
#     # Print the result
#     if is_prime and num > 1:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")

# # Get the user input
# num = int(input("Enter a number: "))

# # Call the function with the input number
# check_prime(num)

        
    

# # Create a function count_vowels(s) that counts and returns the number of vowels in a given string.
# # def count_vowels(s):
# #     vowels = 'aeiouAEIOU'
# #     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# # Example usage
# s = input("Enter a string: ")
# vowel_count = count_vowels(s)
# print(f"The number of vowels in the string is: {vowel_count}")
##############################################################################################
#################################################################################################
# Write a function reverse_string(s) that reverses a given string and returns it.
# def reverse_string(s):
#     s= input("enter a string: ")
#     print(s[::-1])
# reverse_string("s")
# Advanced Questions
# Create a function find_common_elements(list1, list2) that returns a list of common elements between two lists.
# def find_common_elements(list1, list2):
#     # Use set intersection to find common elements
#     return list(set(list1) & set(list2))

# # Example usage
# list1 = [6, 7, 9, 5, 7, 6, 8]
# list2 = [6, 8, 5, 4, 3, 9, 1]

# common_elements = find_common_elements(list1, list2)
# print(f"Common elements between {list1} and {list2} are: {common_elements}")


##############################################
#########################################
# import math
# radius= int(input("enter the radius: "))
# def area_of_circle(radius):
#     print(3.14159 * radius **2)

# area_of_circle(radius)
######################################
################################
# def area_of_rectangle(length,width):
#     # area_of_rectangle= length*width
#     print(f"area of rectangle is : {length*width}")
# area_of_rectangle(7,8)
#################################################
###################################################
# num = [4,8,15,16,23,42]
# def find_mean(num):
#     print(f"{sum(num)/len(num)}")
# find_mean(num)
##############################################
#################################################
# base = int(input("enter a base of triangle: "))
# height= int(input("enter a height of triangle: "))
# def area_of_triangle(base,height):
#     print(f"area of triangle is {1/2*base*height}")
# area_of_triangle(base,height)

###################################3
# var1 = input("enter a character")
# var2 = input("enter second character")
# var1,var2= var2,var1
# print(var1)
# print(var2)
#########################################
##########################################
# import random
# randum_number = random.randint(1,100)
# print(randum_number)
###########################################
##########################################
# kilometers = int(input("enter distance in kilometers: "))
# miles= kilometers*0.621371
# print(f"given kilometer is equal to {miles}")
#################################################
#####################################################
# num = int(input("Enter a number: "))

# if num == 1:
#     print(f"{num} is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")
#####################################################
#######################################################
# Function to check if a number is prime
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#              return False
#     return True

# # Printing prime numbers in the range 1 to 10
# for num in range(1, 11):
#     if is_prime(num):
#         print(num)
####################################################
#########################################################
# num = int(input("enter a number: "))
# factorial= 1
# if num<0:
#     print("please enter positive number")
# elif num==0:
#     print("factorial of 0 is 1")
    
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print(factorial)
###############################################
#############################################
# def found_factorial(num):
#     if num < 0:
#         print("Please provide a positive value, we can't find the factorial of a negative number.")
#     elif num == 0:
#         print("Factorial of 0 is 1")
#     else:
#         factorial = 1
#         for i in range(1, num + 1):
#             factorial *= i  # Multiply the current value of factorial by i
#         print(f"Factorial of {num} is {factorial}")

# # Input number
# num = int(input("Enter a number: "))

# # Call the function
# found_factorial(num)
#######################################################################
########################################################################
#write a python program to find sum of natural number.?
# def sum_of_n(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# n = int(input("Enter any number: "))
# print("Sum of natural numbers ", n, "is:", sum_of_n(n))
# n = int(input("Enter any number: "))
# def  sum_of_n(n):
#     # n = int(input("Enter any number: "))
#     sum=0
#     for i in range(1,n+1):
#         sum = n+i
#         print(sum)
#         sum_of_n(n)
#############################################
#############################################

# n = int(input("Enter a number: "))
# factorial = 1
# n = int(input("Enter a number: "))
# def factorial(n):
#     factorial = 1
#     for i in range(1, n+1):  
#         factorial *= i  
#     print(f"Factorial of {n} is: {factorial}")

# factorial(n)
#############################################
#####################################
# write a functifibonancion which take input from user as a number and find out whether the number is armstrong number is not 
# num= int(input("enter a number: "))
# num= int(input("enter a number: "))
# def find_armstrong(num):
#     num_str = str(num)
#     num_len = len(num_str)
#     sum = 0
#     for digit in num_str:
#         sum += int(digit) ** num_len
#     if sum == num:
#         print("This is an Armstrong number")
#     else:
#         print("This is not an Armstrong number")
#         # num= int(input("enter a number: "))
# find_armstrong(153)

#  write a function  take input from user two number and print fib
# def fibonacci(n1,n2,n3):
#     # n=int(input("enter a number: "))
#     while fibonacci <n3:
#      n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3
# # n = int(input("Enter the number : "))
# print(fibonacci(2,3,5))

# using for loop
# def fibonanci(n1,n2,count):
#      a=n1
#      b=n2
#      for i in range((count)):
#          n3=n1+n2
#          print(n3)
#          n1=n2
#          n2=n3
# print (fibonanci(2,3,5))
# Addition Function Write a function that takes two numbers as arguments and returns their sum.
# def addition():
#     num1= int(input("enter a number: "))
#     num2= int(input("enter a number: "))
#     print(f"num1 + num2 is : {num1+num2}")
# addition()
# Greeting Function Write a function that takes a person's name as an argument and prints a greeting message.
# def greet():
#     name = input("enter any name: ")
#     print(f"hello {name},good morning")
# greet()
# Square Function Write a function that takes a number as an argument and returns its square.
# def square():
#     num= int(input("enter a number: "))
#     print(f"square of {num} is :{num**2}")
# square()
# Length of String Write a function that takes a string as an argument and returns its length.
# def length():
#     str1= input("enter a string: ")
#     print(f"length of string is : {len(str1)}")
# length()
# Even or Odd Write a function that takes a number as an argument and returns True if it's even and False if it's odd.
# def find_even_odd():
#     num= int(input("enter a number: "))
#     if num % 2 ==0:
#         return True
#     else:
#         return False
# # print(find_even_odd())
# Multiplication Table Write a function that prints the multiplication table for a given number up to 10
# def table():
#     num= int(input("enter a number: "))
#     for i in range(1,11):
#         print(f"{num*i}")
# table()
# using while loop.
# def table_num():
#     n= int(input("enter a number: "))
#     count=1
#     while count<11:
#         print(f"{n*count}")
#         count+=1
# table_num()
# Factorial Write a function that takes a number as an argument and returns its factorial.
# num = int(input("Enter a number: "))

# def factorial_num():
#     num= int(input("enter a number: "))
#     factorial = 1
#     for i in range(1, num + 1):  # Loop from 1 to num
#         factorial *= i  # Multiply factorial by i for each iteration
#     return factorial

# # Call kr rha hu function ko
# print(factorial_num())

        
# Reverse String Write a function that takes a string as an argument and returns it reversed.
# def reversed():
#     str2=input("enter a string: ")
#     print(f"{str2[::-1]}")
# reversed()

# Find Maximum Write a function that takes three numbers as arguments and returns the maximum of the three.
# def find_max(num1,num2,num3):
#     print(max(num1,num2,num3))
# find_max(num1=2,num2=6,num3=8)
    
# # # Check Prime Write a function that takes a number as an argument and returns True if it's a prime number, and False otherwise. 
# def prime_num(num):
#     if num<=1:
#         return False
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num%i ==0:
#                 return False
            
#         return True
# print(prime_num(num=21))
# def prime_num():
#     num= int(input("enter a number: ")) 
#     if num<=1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%i ==0:
#                 return False
#         return True
# print(prime_num())
#########################################
###########################################33
# Convert Fahrenheit to Celsius Write a function that takes a temperature in Fahrenheit and returns the temperature in Celsius.
#The formula to convert Celsius to Fahrenheit is: f = 9/5 x c +32
# Function to convert Fahrenheit to Celsius
# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (5/9) * (fahrenheit - 32)
#     return celsius

# # Take user input for temperature in Fahrenheit
# fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# # Convert and print the result
# celsius = fahrenheit_to_celsius(fahrenheit)
# print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius")

# Palindrome Check Write a function that takes a string as an argument and returns True if the string is a palindrome and False otherwise.
# def string():
#     string = input("enter a string: ")
#     if string[::-1] == string:
#         return True
#     else:
#         return False
# print(string())
# Count Vowels Write a function that takes a string as an argument and returns the number of vowels in the string.
# def count_vowel():
#     string = input("Enter a string: ")
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
# print("Number of vowels:", count_vowel())
# Find Minimum Write a function that takes a list of numbers as an argument and returns the smallest number in the list.
# list = [17,8,9,10]
# def find_smallest():
#     print(min(list))
# find_smallest()

# Sum of List Write a function that takes a list of numbers as an argument and returns the sum of all the numbers in the list.
# list = [17,8,9,10]
# def sum_list():
#     print(sum(list))
# sum_list()
# Generate Fibonacci Sequence Write a function that takes an integer n as an argument and returns a list of the first n numbers in the Fibonacci sequence.
# def fibonanci(n1,n2,count):
#      a=n1
#      b=n2
#      for i in range((count)):
#          n3=n1+n2
#          print((n3))
#          n1=n2
#          n2=n3
# print (fibonanci(2,3,5))

## Python program to display all the prime numbers within an interval
# Python program to display all the prime numbers within an interval

# def prime_num(start, end):
#     # start = 1
#     # end = 100
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, num+1 ):
#                 if num % i == 0:
#                     break
#             else:
#                 print(num)
# prime_num(1, 100)
# start = 1
# end = 50

# def prime_number(start, end):
#     for num in range(start, end + 1):
#         if num > 1:  
#             for i in range(2, num):  
#                 if num % i == 0:  
#                     break
#             else:  
#                 print(num)  

# prime_number(start, end)
################################################
#####################################
# def capitalize_first_letter(text):
#     return text.title()
# input_string = "hello world"
# result = capitalize_first_letter(input_string)
# print(result)
#####################################################
###################################################
#

