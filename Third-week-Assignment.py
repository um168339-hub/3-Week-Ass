# 1). Even or Odd Checker

num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 2). Positive, Negative, or Zero Checker

# Take a number as input
num = float(input("Enter a number: "))

# Check if number is positive, negative, or zero
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
# 3
password="umar@312"
guesspassword= input("enter the password")
if password == guesspassword:
    print("Access Granted")
else:
    print("Access Denied")


# 5). # Age Category Finder

# Ask the user for their age
age = int(input("Enter your age: "))

# Check age category using if-elif-else
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior")


# 6). # Number Guessing Game

secret_number = 7

guess = int(input("Guess the number: "))  # Initialize guess variable

 #Keep asking until the user guesses correctly
while guess != secret_number:
    print("Wrong guess, try again!")
    guess = int(input("Guess the number: "))

#When correct
print("Correct! You guessed the number!")

#7
count = 1
username= "umarmughal312"
passs=4488
while count <= 3 :
    usname=input("enter your username")
    passs = input("enter your passs ")
    if passs and usname == username :
        print(" welcome ")
        break
    count+=1
else:
    print(" accountlockes ") 

# 9). Multiplication Table Generator (Using while loop)

num = int(input("Enter a number: "))  # Ask the user for a number

i = 1  # Initialize counter

# Print table up to 10
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
 