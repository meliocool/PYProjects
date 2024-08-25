# ______ __   __ _____  _   _  _____  _   _ 
# | ___ \\ \ / /|_   _|| | | ||  _  || \ | |
# | |_/ / \ V /   | |  | |_| || | | ||  \| |
# |  __/   \ /    | |  |  _  || | | || . ` |
# | |      | |    | |  | | | |\ \_/ /| |\  |
# \_|      \_/    \_/  \_| |_/ \___/ \_| \_/
                                          
import math
import time
import random
import os
import shutil

# --- VARIABLES --- #
# Used to store data like in C

name = "Dhitan" # String
age = 19 # Integer
height = 165.7 # Float
attractive = False # Boolean

# print("Hi my name is", name, "I am " + str(age) + " years old", "and i am " + str(height) + " cm tall") # Print statement ex

# --- STRING MANIPULATION --- #
# String are texts noted by "" or ''

text = "Go Youn-Jung"
# # Length of the string (includes spaces as well)
# print(len(text))
# # Find a character in a string
# print(text.find("o"))
# # Capitalize the first letter in the string
# print(text.capitalize())
# # Uppercase all characters
# print(text.upper())
# # Lowercase all characters
# print(text.lower())
# # Check if string is only ALPHABETICAL letters NO spaces
# print(text.isalpha())
# # Counting how many certain characters are in the string
# print(text.count("o"))
# # Replace character in the string
# print(text.replace("o", "a"))
# # Multiply string by a certain number to print it a number of times
# print(text*3)

# --- USER INPUTS --- #
# Receive an input from the user like scanf() in C

# level = int(input("What is your current level in Elden Ring? "))
# build = input("What is your current Elden Ring Build? ")
# print("Currently you are level " + str(level) + " with a " + build + " build")

# --- MATH FUNCTIONS --- #
number = 3.14
num1 = 1
num2 = 2
num3 = 690
# # Round
# print(round(number))
# # Round up
# print(math.ceil(number))
# # Round down
# print(math.floor(number))
# # Absolute value of a number
# print(abs(number))
# # Raise a base number to an exponent
# print(pow(number, 2))
# # Square root
# print(math.sqrt(9))
# # Find the largest of some values
# print(max(num1,num2,num3))
# # Find the smallest of some values
# print(min(num1, num2, num3))

# --- STRING SLICING --- #
# Indexing[] or slice()
# [start:stop:step]

char = "An Yujin"

first_name = char[:2]
last_name = char[3:]
reverse_char = char[::-1]
website = "https://www.jype.com"
webName = slice(12,-4)

# print(first_name)
# print(last_name)
# print(reverse_char)
# print(website[webName])

# --- IF STATEMENTS --- #
# if elif else

# favIdol = input("Who is your favorite Idol? ")
# if favIdol == "Lisa" or favIdol == "Jisoo" or favIdol == "Jennie" or favIdol == "Rose":
#     print("Fuck you Blink!")
# elif favIdol == "Jeongyeon" or favIdol == "Seeun":
#     print("You just like me fr")
# else:
#     print("Nice! :D")

# --- LOOPING --- #
# WHILE LOOP
# Execute a block of code while the condition remains true

idol = None
# while not idol:
#     idol = input("Who is your favorite Idol? ")
# print("Your favorite idol is " + idol)

# FOR LOOP
# Same as while but with a limit

idolName = "An Yujin"
# for i in range(10):
#     print(i+1)
# for i in range(50, 100, 2):
#     print(i)
# for i in idolName:
#     print(i)
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Thanks for waiting!")

# NESTED LOOP
# height = int(input("Enter the height of the Triangle: "))
# symbol = input("Enter a symbol: ")
# for i in range(height + 1):
#     print(symbol * i)

# LOOP CONTROL

## break = exits the loop entirely
# while True:
#     jaeger = input("Enter your favorite Jaeger ")
#     if jaeger != "":
#         break

## continue = skips to the next iteration
# jaeger_code = "G1P5Y-D4NG3R-234-15"
# for i in jaeger_code:
#     if i == "-":
#         continue #SKIPS THE ITERATION IF ITS -
#     print(i) 

## pass = does nothing
# for i in range(1, 20):
#     if i == 13:
#         pass
#     else:
#         print(i)

# --- LIST --- #
# SAME AS ARRAY, STORE MULTIPLE ITEMS IN A VARIABLE

anime = ["Bleach", "Kimi ni Todoke", "Kami no Tou", "Mob Psycho 100"]
# anime.append("Boku no Hero Academia") # ADD AN ELEMENT AT THE END
# anime.remove("Kimi ni Todoke") # REMOVE A CERTAIN ELEMENT IN THE LIST
# anime.pop() # REMOVE THE LAST ELEMENT
# anime.insert(0, "Tokyo Ghoul") # INSERT AN ELEMENT AT THE GIVEN INDEX
# anime.sort() # SORT ALPHABETICALLY
# anime.clear() # CLEAR THE WHOLE LIST
# for i in anime:
#     print(i, end=" ")

# 2D LISTS
ThirdGen = ["TWICE", "Red Velvet", "Blackpink"]
FourthGen = ["NewJeans", "NMIXX", "STAYC"]
GirlGroups = [ThirdGen, FourthGen]
# print(GirlGroups)
# print(GirlGroups[0][0]) # KINDA LIKE AN 2D MATRIX IN C

# --- TUPLE --- #
# Collection which is ordered and unchangeable used to group related data

homie = ("Nico",  19, "Male")
# if "Nico" in homie:
#     print("Fat ass mf is my homie")

# --- SET --- #
# Unordered collection, unindexed, and no duplicate values

nmixx_member = {"Lily", "Haewon", "Sullyoon", "Bae", "Jiwoo", "Kyujin"}
twice_member = {"Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"}
twice_member.add("Baraqbah") # add a new element to the set
twice_member.remove("Baraqbah") # Remove a certain element
twice_member.update(nmixx_member)
jyp_Group = twice_member.union(nmixx_member)

# print(twice_member.difference(nmixx_member)) # What twice has that nmixx doesnt
# print(twice_member.intersection(nmixx_member)) # What they both have in common
# for i in jyp_Group:
#     print(i) # Will print in random order

# --- DICTIONARY --- #
# A changeable and fast unordered collection of unique key:value because they use hashing

aceGroups = {'YG':'Big Bang', 
             'JYP': 'TWICE',
             'SM': 'EXO',
             'HYBE': 'BTS'}
aceGroups.update({'Starship':'IVE'})
aceGroups.update({'HYBE': 'NewJeans'})
aceGroups.pop('HYBE')

# print(aceGroups["JYP"])
# print(aceGroups.get("Starship")) # Check if there is a key Starship
# print(aceGroups.keys()) # Print the keys
# print(aceGroups.values()) # Print the values
# print(aceGroups.items()) # Print everything

# for key,value in aceGroups.items():
#     print(key,value)

# --- INDEX OPERATOR ---- #
# Access to each element inside a string, list, or tuples

aespa_mem = "karina"
if aespa_mem[0].islower():
    aespa_mem = aespa_mem.capitalize()
     
# print(aespa_mem)

first_three = aespa_mem[0:3].upper()
last_three = aespa_mem[3:].upper()
last_char = aespa_mem[-1] # Negative indexing for the last character

# print(first_three)
# print(last_three)
# print(last_char)

# --- FUNCTION --- #
# a block of code that only executed when called

def susein(x, y, z, n):
    return (x * y + z) / n

# print(int(susein(8, 4, 4, 6)))

# --- NESTED FUNCTION CALLS --- #
# returned value from another function can be used as an argument in the parameter of other functions

# what = input("Enter a number: ")
# print(round(abs(float(what))))

# The code above would first get an input stored in what and then print the inputted number but before that
# it turns it into a float, then find the absolute form, and then round it to the nearest whole number

# --- VARIABLE SCOPE --- #
# A variable is only recognized inside a region it was declared
# Local variable is INSIDE of a function
# Global variable is available INSIDE and OUTSIDE of any function because its declared outside

aidoru = "Jang Vicky"
def display_Idol():
    aidoru = "An Yujin"
    print(aidoru)

# display_Idol()
# print(aidoru)

# --- *ARGS --- #
# *args is a parameter that will pack all given arguments into a tuple
# useful because functions can now accept varying amount of arguments
# args can be changed into other the important thing is the asterisk

def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
# print(addition(1,2,3,4,5))

# To change certain elements in the args tuple, typecast it into List first
def addition2(*args):
    sum = 0
    args = list(args)
    args[0] = 0 # Changes the first element into 0
    for i in args:
        sum += i
    return sum
# print(addition2(1,2,3,4,5)) # So 1 becomes 0 in this case 

# --- **KWARGS --- #
# **kwargs is a parameter that will pack all arguments into a dictionary
# useful because a function can now accept varying amounts of KEYWORD as arguments

def homieName(**homie):
    print("Your Homie's name is", end=" ")
    for key,value in homie.items():
        print(value, end=" ")

# firstName = input("What is your Homie's first name? ")
# confirmation = input("Does your Homie have a middle name? ")
# nameSections = {"First":firstName}
# if confirmation == "Y":
#     middleName = input("What is their middle name? ")
#     nameSections["Middle"] = middleName
# else:
#     pass
# lastName = input("What is their last name? ")
# nameSections["Last"] = lastName
# homieName(**nameSections)

# --- STRING FORMATTING --- #
# {} format fields in a string
groupName = "IVE"
biasName = "An Yujin"
# print("I love {} from {}".format("An Yujin", "IVE"))
# print("I love {} from {}".format(biasName, groupName))
# print(f"I love {biasName} from {groupName}")
yap = "I love {} from {}"
# print(yap.format(biasName, groupName))
# Some spaces or padding between the texts
# print("I love {:10} from {:10}".format(biasName, groupName))
# print("I love {:<10} from {:<10}".format(biasName, groupName))
# print("I love {:>10} from {:>10}".format(biasName, groupName))
# print("I love {:^10} from {:^10}".format(biasName, groupName))
# Formatting numbers
numba = 3.14159
numba2 = 1000000000
# print("Pi is {:.2f}".format(numba))
# print("The number in thousands is {:,}".format(numba2)) # Automatically adds comma in every thousands
# print("The number in Binary is {:b}".format(numba2)) # Display number as Binary
# print("The number in Octal is {:o}".format(numba2)) # Display number as octal
# print("The number in Hexadecimal is {:X}".format(numba2)) # Display number as Hexadecimal
# print("The number in Scientific Notation is {:e}".format(numba2)) # Display number as scientific notation

# --- PSEUDO RANDOM NUMBER --- #
x = random.randint(1,6) # random number from 1 to 6
y = random.random() # random number from 0 to 1
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards) # shuffle cards

# --- EXCEPTION HANDLING --- #
# Exception = Eveent detected during execution that interrupt the normal flow of the program
# try will be used to wrap a 'dangerous' code
# try:
#     numerator = int(input("Enter a numerator: "))
#     denominator = int(input("Enter a denumerator: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero!")
# except ValueError as e:
#     print(e)
#     print("Numbers only please!")
# except Exception as e:
#     print(e)
#     print("Something went wrong! :(")
# else:
#     print(result)

# --- PLAYING WITH FILES --- #
# Make sure to import os and shutil first

# FILE DETECTION
path = "C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\IMAGES\\PolynomialRegression.png"
# if os.path.exists(path):
#     print("That file exists!")
#     if os.path.isfile(path):
#         print("It is a file!")
#     elif os.path.isdir(path):
#         print("It is a folder!")
# else:
#     print("Doesn't exist T-T")

# FILE READING
# try:
#     with open('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\triplesot24.txt') as file:
#         print(file.read()) # Closed Automatically after Opened
# except FileNotFoundError:
#     print("That file was not found")

# FILE WRITING
ot10 = "S1 = SeoYeon\nS2 = Hyerin\nS3 = Jiwoo\nS4 = ChaeYeon\nS5 = YooYeon\nS6 = SooMin\nS7 = NaKyoung\nS8 = YuBin\nS9 = Kaede\nS10 = DaHyun"
with open('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\triplesot10.txt', 'w') as file:
    file.write(ot10)

# FILE COPYING
# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

# source, destination
shutil.copyfile('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\triplesot10.txt', 'C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\triplesot10Copy.txt')

# FILE MOVING
SourceFile = "C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\SeoYeonVictory.png"
destinationFile = "C:\\Users\\Asus VivobookPro\\Pictures\\Screenshots\\Screenshot (1196).png"
# try:
#     if os.path.exists(destinationFile):
#         print("There is already a file with the same name")
#     else:
#         os.replace(SourceFile, destinationFile)
#         print(SourceFile + " has been successfully moved!")
# except FileNotFoundError:
#     print(SourceFile + " Not found!")

# FILE DELETION

toBeDel = "C:\\Users\\Asus VivobookPro\\Pictures\\Screenshots\\Screenshot (967).png"
# try:
#     os.remove(toBeDel) # remove a file
#     os.rmdir(toBeDel) # remove an empty directory / folder
#     shutil.rmtree(toBeDel) # Considered Dangerous, remove the entire directory containing the file
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission!")
# except OSError:
#     print("You cannot that file using that function")
# else:
#     print("File successfully deleted!")

# --- MODULE PROGRAMMING --- #
# importing a module means using functions from other python files
# import moduleTest as mt
# from moduleTest import * # IMPORT EVERYTHING
# from moduleTest import Hi # IMPORT THE HI FUNCTION
# mt.Hi()

# --- OOP WITH PYTHON --- #
