
# Que 1: Age group categorization

'''age = int(input("Enter Your Age :"))

if age < 13:
    print("Child")
elif age < 20 :
    print("Teenager")
elif age < 60 :
    print("Adult")
else:
    print("Senior") '''

# Que 2 :Movie Tichet pricing
'''
import datetime

age = int(input("Enter Your Age :"))

today = datetime.datetime.today()

day_of_week = today.strftime('%A')

price = 12 if age >= 18 else 8


if day_of_week == "Wednesday" :
    # price -= 2
    price = price - 2

print("Today is",day_of_week)
print("Ticket price for You is $",price)
'''

#Que 3 Grade Calculator
'''
score = int(input("Enter Your Score :"))

if score > 100:
    print("Invalid Input Please Enter Score upto 100 ...")
    exit()

if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"
print("Grade:",grade)
'''

# Que 4 Fruit Ripeness Checker

#condition_of_f


#Que 5 Leap Year

year = int(input("Enter Year To Check Wheater It Is Leap Year Or Not :"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year..")
else:
    print(year,"is NOT a leap year...")

