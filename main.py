# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # # 100 days of python exercise 
# print("Hello\nWorld!")
# print("Hello " + "Angela")
# print("Hello " + input("what's your name? ") + "!")
# print(len(input("What's your name? ")))
# #write a program that switches a and b value around
# a = input("a: ")
# b = input("b: ")
#
# c = a
# a = b
# b = c
#
# print("a = " + a)
# print("b = " + b)

# print("Welcome to band name generator!")
# city = input("Which city did you grew up in?\n")
# pet = input("What's the name of your favorite pet?\n")
# print("your bank name is " + city + " " + pet)
# print("Hello"[-2])
# print("123456789"[4])
# user_num = input("What's your number? ")
# print(int(user_num[0]) + int(user_num[1]))

# # PEMDAS operating rule: parenthesis exponent multiplication division addition subtraction
# # below is a BMI calculator
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2, 2)
#
# if bmi < 18.5:
#     print(f"Your BMI is: {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is: {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is: {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your BMI is: {bmi}, you are obese.")
# else:
#     print(f"Your BMI is: {bmi}, you are clinically obese.")



#floor division is // , for example 8//3 = 2
# use previous result: += -= /= *=
#f-string allows to print string, integer, float and boolean.

# age = int(input("What's your current age? "))
# daysleft = (90 - age) * 365
# monthsleft = (90 - age) * 12
# weeksleft = (90 - age) * 52
# message = f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left"
# print(message)

# #Tip calculator
# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? $") )
# tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
# people = int(input("How many people to split the bill? "))
# #pay = round(bill * (1 + tip)/people, 2)
# pay = "{:.2f}".format(bill * (1 + tip)/people, 2)
# message = f"Each person should pay ${pay}"
# print(message)

# # # if / else and Conditional operators
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What's your age? "))
#     if age < 12:
#         bill = 5
#         print("child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print("You got to ride for free!")
#     else:
#         bill = 12
#         print("adult tickets are $12.")
#
#     photo = input("Do you want a photo taken? Y or N ").lower()
#     if photo == "y":
#         bill += 3
#
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")
    
# # Odd or even number check, use modulo  which is written as a percentage sign % in python.
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# Nested if / else
# # leap year
# year = int(input("which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This is a leap year.")
#         else:
#             print("This is NOT a leap year.")
#     else:
#         print("This is a leap year.")
# else:
#     print("This is NOT a leap year.")

# # Pizza ordering program
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S M or L ").lower()
# add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N "). lower()
# bill = 0
# if size == "s":
#     bill += 15
#     if add_pepperoni == "y":
#         bill += 2
# elif size == "m":
#     bill += 20
#     if add_pepperoni == "y":
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == "y":
#         bill += 3
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")

# logical Operators and or not
# # Love calculator
# print("Welcome to the Love calculator!")
# name1 = input("What is your name \n").lower()
# name2 = input("What is their name \n").lower()
# names = name1 + name2
#
# true_string = "true"
# count1 = 0
# for i in range(0, len(true_string)):
#     x = names.count(true_string[i])
#     count1 += x
# # print(count1)
#
# love_string = "love"
# count2 = 0
# for i in range(0, len(love_string)):
#     x = names.count(love_string[i])
#     count2 += x
# # print(count2)
# score = int(str(count1)+str(count2))
# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"your score is {score}.")
#
# # treasure island game
# print("welcome to Treasure Island.\nYour mission is to find the treasure.")
# step1 = input("Do you want to go left or right? L or R ").lower()
# if step1 == "l":
#     step2 = input("do you want to wait for a boat or swim across? W or S ").lower()
#     if step2 == "w":
#         step3 = input("There are 3 doors. Red, Yellow and Blue. Which one do you choose? R, Y, or B ").lower()
#         if step3 == "y":
#             print("You win!")
#         else:
#             print("Game over.")
#     else:
#         print("Game Over.")
# else:
#     print("Game over.")

# # Randomisation and Python lists
# import random
# random_integer = random.randint(1,10)
# print(random_integer)

bah_is_five = False

while not bah_is_five:
    bah = 2 + 3
    if bah == 5:
        bah_is_five = not bah_is_five

print(bah)

