# Que 1 Counting Positive Numbers From List

'''num = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0

for number in num:
    if number > 0:
        positive_number_count += 1
print("Final count of Positive numbers is :",positive_number_count)'''

# Que 2 Sum of even numbers

'''n = int(input("Enter the range of number:"))

sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0 :
        sum_even += i

print("Sum of even number is :",sum_even)
'''
# Que 3 Multiplication table upto 10(skip 5th iteration)

'''num = int(input("Enter the number :"))

for i in range(1, 11):
    if i == 5:
        continue  # to skip iteration
    print(num, '*' ,i,'=', num * i)'''

#Que 4 Reverse String

'''input_str ="Apurva"

reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(reversed_str) '''

#Que 5 Find the First Non-Repeated Character

'''input_str = "Queen"

for char in input_str:
    if input_str.count(char) == 1:
        print("The Non-Repeated Character is :",char)
        break
'''

# Que 6 Factorial Calculator

# number = int(input("Enter a number :"))

# factorial = 1

# for i in range(1, number+1):
#     factorial *= i

# print("Factorial is :",factorial)

'''while number > 0:
    factorial = factorial * number
    number = number - 1

print('Factorial of',number,'is:',factorial)
'''

#ue 7 take input from user upto it not gives number between 1 to 10
'''
while True:
    number = int(input("Enter Value Between 1 To 10 :"))

    if 1 <= number <= 10 :
        print("Thanks")
        break
    else:
        print("Invaid Input.. Try Again")
        '''

# Que 8 Prime number checker

# number = int(input("Enter a number to check wheather it is prime or not :"))

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)

'''for i in range(2, number//2+1):
    if (number % i) == 0:
        print(number,'is not a prime...')
        break
else:
     print(number,'is a Prime')
'''

#Que 9 Exponential BackOff

import time

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("Attempt",attempt + 1, "- wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1


#Que 10

for line in open('list.py'):
    print(line, end=(''))