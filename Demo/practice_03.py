#Que 1 written square of numbers

def square_of_numbers (number) :
    #  print(number ** 2)
    return number ** 2

# square_of_numbers(4)
result = square_of_numbers(4)
print(result)

# Que 2 Sum of 2 numbers

def add (num1, num2):
    return num1 + num2

addition = add (21, 22)
print(addition)

# Que 3 multiply of 2 numbers

def multiply (p1, p2):
    return p1 * p2

print(multiply(21, 22))
print(multiply('a', 5))
print(multiply(10, 'r'))

# Que 4 Area and Circumference of circle

import math

def circle_cal (radius) :
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference

a, c = circle_cal(10.5)

# a = round(a, 2)
# c = round(c, 2)

print("Area of Circle is :",a,'Circumference of Circle is :',c)
print(f"Area of Circle is: {a:.2f}, Circumference of Circle is: {c:.2f}")

#Que 5

def greet (name = 'User'):
    return "Hello, " + name + "!!!"

print(greet("Good Morning Everyone"))
print(greet())

#Que 6  Lambda Function

cube = lambda x : x ** 3

print(cube(15))

# Que 6 Multipal Arguments

def sum_all (*args):
    print(args,type(args))
    for i in args:
        print(i ** 3)
    return sum(args)

print(sum_all(1, 2, 6, 8))

#Que 7 

def print_kwargs (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name = "Shaktiman", power = "Lazer")
print_kwargs(name = "Shaktiman")
print_kwargs(name = "Shaktiman", power = "Lazer", enemy = "Dr. Jackaal")

#Que 8

def even_generator(limit):

    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

#Que 9 Recursive Function
    
def factorial (n):

    if n == 0:
        return 1
    else:
         return n * factorial(n-1)

x = int(input("Enter a number to calculate factorial:"))
print("Factorial of ",x, ":",factorial(x))