# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:26:09 2024

@author: dhanu
"""

# main.py


from divisibility import is_divisible

number = int(input("Enter a number: "))
if is_divisible(number):
    print(f"{number} is divisible by 2.")
else:
    print(f"{number} is not divisible by 2.")

s="abcdefgh"
print(s[::2])
