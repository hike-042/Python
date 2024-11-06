# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:41:59 2024

@author: dhanu
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):

    print(year, "is a leap year.")

else:

    print(year, "is not a leap year.")
