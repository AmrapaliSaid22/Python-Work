# def favorite_color_message(color):
#     if color.lower() == "red":
#         return "Red is a bold color!"
#     elif color.lower() == "blue":
#         return "Blue is a calm color!"
#     elif color.lower() == "green":
#         return "Green is associated with nature and growth!"
#     else:
#         return f"{color} is an interesting choice!"

# def main():
#     favorite_color = input("What is your favorite color? ")
#     message = favorite_color_message(favorite_color)
#     print(message)

# if __name__ == "__main__":
#     main()
# a = input("Please enter your favourite color Blue/Red/Black = ").lower()

# ABC -> abc
# Black -> black

# if a == "blue":
#     print("Blue is a calm color ")
# elif a == "red":
#     print("Red is a bold color")
# elif a == "black":
#     print("Black is class")
# else:
#     print("Please enter color given in the list")

  # Prompt the user to input a number, and convert the input to a floating-point number.
# num = float(input("Input a number: "))

# # Check if the number is greater than zero.
# if num > 0:
#    # If true, print that it is a positive number.
#    print("It is a positive number")
# # Check if the number is equal to zero.
# elif num == 0:
#    # If true, print that it is zero.
#    print("It is zero")
# else:
#    # If the above conditions are not met, print that it is a negative number.
#    print("It is a negative number")

#License: https://bit.ly/3oLErEI

# def test(nums):
#     return ["A+" if grade >= 4.0
#             else ("A" if grade >= 3.7
#                   else ("A-" if grade >= 3.4
#                         else ("B+" if grade >= 3.0
#                               else ("B" if grade >= 2.7
#                                     else ("B-" if grade >= 2.4
#                                           else ("C+" if grade >= 2.0
#                                                 else ("C" if grade >= 1.7
#                                                       else ("C-" if grade >= 1.4
#                                                             else "F"))))))))
#             for grade in nums]

   
# nums = [4.0, 3.5, 3.8]
# print("List of numbers:",nums)
# print("Convert GPAs to letter grades:")
# print(test(nums))
# nums = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
# print("\nList of numbers:",nums)
# print("Convert GPAs to letter grades:")
# print(test(nums))

# Prompt the user to enter four ages
# age1 = int(input("Enter age 1: "))
# age2 = int(input("Enter age 2: "))
# age3 = int(input("Enter age 3: "))
# age4 = int(input("Enter age 4: "))

# # Compare the ages to find the youngest age
# youngest_age = min(age1, age2, age3, age4)

# # Print out the youngest age
# print("The youngest age is:", youngest_age)

# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,9))
