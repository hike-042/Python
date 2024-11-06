# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:00:34 2024

@author: dhanu
"""
s=0
for i in range(5):
    s=s+i
print (s)

print("\n")



n=5
while n>0:
    print(n)
    n-=1


n=2
while n<6:
    print(n)
    n+=1


def greet(name):
    print("Hello", name)
    
greet("Dhanush")

def greet(name):
    for i in range(4):
        print(f"Hello {name}")
greet("Dhanush")


fruits = ["apple","banana","cherry"]
print(fruits)

fruits.append("orange")
print(fruits)

fruits.remove("apple")
print(fruits)

person={
        "Name":"Dhanush Kumar R",
        "Age" :"21",
        "City" : "Madurai",
        "State" : "Tamil Nadu",
        "Degree" : "B.E MBA",
        }

print(person.get("Name"))
print(person.get("Age"))
print(person.get("City"))
print(person.get("State"))
print(person.get("Degree"))

text = "Hello Dhanush"
print(text.upper())
print(text.lower())
print(text.replace("Hello","Nothing"))


with open("sample.txt","w") as file:
    file.write("This is a sample text")
    


correct_pass = "Pesu@123"
attempts = 0
while attempts < 2:
    password = input("Enter the Password carefully:\t")
    if password == correct_pass:
        with open("sample.txt","w") as file:
            file.write("This file is granted")
        print("Access Granted")
    else:
        print("Incorrect Password!!")
        attempts+=1
else:
    print("Sorry You are not Logged in")
    

s=0
n = int(input("Enter the number"))
i=n
while(n!=0):
    
    d=n%10
    s=s*10+d
    n//=10

if (s==i):
    print("Palindrome")
else:
    print("Not a palin")
    
str1=input("Enter the String 1")

if(str1==str1[::-1]):
    print("The word is a palindrome")
else:
    print("The word is not palindrome")
   
    
last_name_has_a = input("Enter last name:\t")
if (last_name_has_a.lower().startswith("a")):
    print("last name starts with a")
if (last_name_has_a.lower().endswith("a")):
    print("Last name ends with a")
if "a" in last_name_has_a:
    print("A is in the word")
count_a = last_name_has_a.count("a")
print(f"Name is {last_name_has_a} and the count of a is: {count_a}")

word = input("Enter the name:\t")
vowels = "aeiou"
count = 0

for letter in word.lower():
    if letter in vowels:
        count += 1

print("The number of vowels in", word, "is:", count)


with open ("C:\\Users\\dhanu\\Downloads\\example.txt","r") as file:
    for line in file:
        print(line.strip())

with open("C:\\Users\\dhanu\\Downloads\\example.txt","w") as file:
    file.write("\nHello, this is a a sample text written in the file.\t\n")
    file.write("\nwriting mulitple lines is also possible.\t\n")
    file.write("\t\nI dont know Coding Leave me alone")
    


def a_sum(x):
    return x+x
a_sum(2)
#lambda function
y=lambda x: x+x
y(2)


y= lambda x: x**3
y(2)
add= lambda x, y: x+y
result = add(2,3)
print(result)


def get_ing(wd):
    return(wd +"ing")
get_ing("go")

m= lambda a: a+ "ing"
m("go")


def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))
#another method
reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))


def is_even(n):
    return n%2 == 1
nums = [1,2,3,4,5,6,7,8]
odds = list(filter(is_even, nums))
print(odds)

nums= [1,2,3,4,5,6,7,8]
odds= list(filter(lambda n: n%2 == 1, nums))
print(odds)


def is_even(n):
    return n%2 == 0
nums = [1,2,3,4,5,6,7,8]
even = list(filter(is_even, nums))
print(even)

nums= [1,2,3,4,5,6,7,8]
even= list(filter(lambda n: n%2 == 0, nums))
print(even)


def update(n):
    return n*2
doubles = list(map(update,nums))
print(doubles)

doubles = list(map(lambda n: n*2, nums))
print(doubles)


nums = [1,2,3,4,5,6,7,8]
incremenated_numbers = list(map(lambda n: n+2, nums))
print(incremenated_numbers)


words = ["cat", "dog", "car", "tree", "book"]
plural= list(map(lambda word: word + 's', words))
print(plural)

words = ["cat", "dog", "car", "tree", "book"]
uppercase= list(map(lambda word: word.upper(), words))
print(uppercase)


subject_marks = [("English", 88), ("Science",90),("Maths",97),("Social Sciences",82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key  = lambda x: x[1]) #marks wise
print("Sorting the list of tuples")
print(subject_marks)

subject_marks = [("English", 88), ("Science",90),("Maths",97),("Social Sciences",82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key  = lambda x: x[0]) #subject wise
print("Sorting the list of tuples")
print(subject_marks)


def switch_case(operations,x,y):
    match operations:
        case 'add':
            return x+y
        case 'sub':
            return x-y
        case 'mul':
            return x * y
        case 'div':
            return x / y if y!=0 else 'Division by zero'
        case 'mod':
            return x//y
        case 'pow':
            return x ** y
        case _:
            return 'Invalid operation'

x=int(input("Enter the Number:\t"))
y=int(input("Enter the Number:\t"))

print(switch_case('add', x, y))
print(switch_case('sub', x, y))
print(switch_case('mul', x, y))
print(switch_case('div', x, y))
print(switch_case('mod', x, y))
print(switch_case('pow', x, y))



def switch_case(operations, x, y):
    match operations:
        case 'add':
            return x + y
        case 'sub':
            return x - y
        case 'mul':
            return x * y
        case 'div':
            return x / y if y != 0 else 'Division by zero'
        case 'mod':
            return x // y
        case 'pow':
            return x ** y
        case _:
            return 'Invalid operation'

# Using lambda to call switch_case
operation_lambda = lambda op, a, b: switch_case(op, a, b)

x = int(input("Enter the first number:\t"))
y = int(input("Enter the second number:\t"))

# Call the lambda function for each operation
print(operation_lambda('add', x, y))
print(operation_lambda('sub', x, y))
print(operation_lambda('mul', x, y))
print(operation_lambda('div', x, y))
print(operation_lambda('mod', x, y))
print(operation_lambda('pow', x, y))



def evaluate_sgpa(sgpa):  
    match sgpa:  
        case sgpa if 8.0 < sgpa < 9.0:  
            return "Congratulations"  
        case sgpa if 7.0 < sgpa < 8.0:  
            return "Very Good"  
        case sgpa if 5.0 < sgpa < 6.0:  
            return "Happy withdrawal"  
        case sgpa if 4.0 < sgpa < 5.0:  
            return "Perfect"  
        case _:  
            return "SGPA is outside the expected range"  

# Example usage  
sgpa = float(input("Enter your SGPA: "))  
result = evaluate_sgpa(sgpa)  
print(result)


num = int(input("Enter the Numebr:\t"))
d=num/10




def find_pairs(target):  
    return [(target * d, d) for d in range(1, 11)]  

target = 21  
result = find_pairs(target)  

for numerator, denominator in result:  
    print(f"{numerator} / {denominator} = {target}")


import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0,6])
ypoints = np.array([0,250])
plt.plot((xpoints,ypoints))
plt.show()    
    
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,6,8,10]

plt.plot(x,y,marker='x')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)
plt.show()


import matplotlib.pyplot as plt  

 
x = [1, 2, 3, 4, 5]  
y = [1, 4, 6, 8, 10]  
plt.bar(x, y)  
plt.xlabel('X-axis')  
plt.ylabel('Y-axis')  
plt.title('Bar Graph Example')  
#plt.grid(axis='y')    
plt.show()

import matplotlib.pyplot as plt
profit = [1000, 2000, 3000, 4000, 5000]
product = ['parle1','parle2','parle3','parle4','parle5']

plt.plot(profit, product, marker='x')
plt.xlabel('Product')
plt.ylabel('Profit')
plt.title('Line Graph of Coordinates')

plt.grid(True)
plt.show()

 
myName=	input("Please enter your name:	")
myAge=	input("What	about your age:	")
print(f"Hello World,\tmy name is\t, {myName},and I am, {myAge},years old.")

try:
    answer=12/0
    print(answer)
except:
    print("ZerodivisonError")
    
try:
    value = int(input("Enter a number: "))
    print(f"You entered: {value}")
except:
    print("ValueError: You must enter a numeric value.")
    
try:
    with open('C:\\Users\\dhanu\\Downloads\\output.txt', 'r') as file:
        content = file.read()
        print(content)
except:
    print("An IOError occurred")

try:
    x=[1,2,3]
    print(x[5])
except IndexError:
    print("Index out of range")
    
    
try:
    num=int("Hello")
except ValueError:
    print("Conversion Failed")
finally:
    print("Enfd")
    
    
text = "Python Programming"
result = text.find("Pro",5,10)
print(result)

my_list=[1,2,3,4]
my_list.append(5)
print(my_list(4))
print(my_list(5))

a="Hello"
b="World"
print(a[-1] + b[1:4])


def add(x,y=10):
    return x+y
print(add(5,z=3))