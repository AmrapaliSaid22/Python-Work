# # Get input from the user
# number = int(input("Enter a number: "))

# # Check the conditions
# if number % 2 == 0 and number % 3 == 0 and number % 8 != 0:
#     print('Yes')
# else:
#     print('No')


# Rent Calculator

# Get input from the user
# num_rooms = int(input("Enter the number of rooms: "))
# cost_per_room = float(input("Enter the cost per room: "))

# # Calculate total rent
# total_rent = num_rooms * cost_per_room

# # Print the result
# print(f"The total rent for {num_rooms} rooms at ₹{cost_per_room:.2f} per room is: ₹{total_rent:.2f}")

# a = 3
# b = (a!=3)
# print(b)

# Get input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
