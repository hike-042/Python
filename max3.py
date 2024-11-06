# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:48:08 2024

@author: dhanu
"""

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:

    largest = num1

elif num2 >= num1 and num2 >= num3:

    largest = num2

else:

    largest = num3

print("The largest number is:", largest)
