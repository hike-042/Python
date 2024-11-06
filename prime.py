# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:10:36 2024

@author: dhanu
"""

def checkIfPrime(numberToCheck):
    for x in range(2, numberToCheck):
        if(numberToCheck%x==0):
            return False
        return True