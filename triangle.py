# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:51:51 2024

@author: dhanu
"""

side1 = float(input("Enter the length of the first side: "))

side2 = float(input("Enter the length of the second side: "))

side3 = float(input("Enter the length of the third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):

    print("The triangle is valid.")

else:

    print("The triangle is not valid.")
