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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# --- USER INPUTS --- #
# Receive an input from the user like scanf() in C

# level = int(input("What is your current level in Elden Ring? "))
# build = input("What is your current Elden Ring Build? ")
# print("Currently you are level " + str(level) + " with a " + build + " build")

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# --- IF STATEMENTS --- #
# if elif else

# favIdol = input("Who is your favorite Idol? ")
# if favIdol == "Lisa" or favIdol == "Jisoo" or favIdol == "Jennie" or favIdol == "Rose":
#     print("Fuck you Blink!")
# elif favIdol == "Jeongyeon" or favIdol == "Seeun":
#     print("You just like me fr")
# else:
#     print("Nice! :D")

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# 2D LISTS
ThirdGen = ["TWICE", "Red Velvet", "Blackpink"]
FourthGen = ["NewJeans", "NMIXX", "STAYC"]
GirlGroups = [ThirdGen, FourthGen]
# print(GirlGroups)
# print(GirlGroups[0][0]) # KINDA LIKE AN 2D MATRIX IN C

#--------------------------------------------------------------------------#

# --- TUPLE --- #
# Collection which is ordered and unchangeable used to group related data

homie = ("Nico",  19, "Male")
# if "Nico" in homie:
#     print("Fat ass mf is my homie")

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# --- FUNCTION --- #
# a block of code that only executed when called

def susein(x, y, z, n):
    return (x * y + z) / n

# print(int(susein(8, 4, 4, 6)))

#--------------------------------------------------------------------------#

# --- NESTED FUNCTION CALLS --- #
# returned value from another function can be used as an argument in the parameter of other functions

# what = input("Enter a number: ")
# print(round(abs(float(what))))

# The code above would first get an input stored in what and then print the inputted number but before that
# it turns it into a float, then find the absolute form, and then round it to the nearest whole number

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# --- PSEUDO RANDOM NUMBER --- #
x = random.randint(1,6) # random number from 1 to 6
y = random.random() # random number from 0 to 1
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards) # shuffle cards

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------#

# --- MODULE PROGRAMMING --- #
# importing a module means using functions from other python files
# import moduleTest as mt
# from moduleTest import * # IMPORT EVERYTHING
# from moduleTest import Hi # IMPORT THE HI FUNCTION
# mt.Hi()

#--------------------------------------------------------------------------#

# --- OOP WITH PYTHON --- #
# Python Object Oriented Programming (POOP) is a way to program a real world object with it's ATTRIBUTES
# and ACTIONS
# Best practice to use different modules for different classes
# import the module
from triples import Member
from humans import Human, NPC, idol, tripleS, hyuna
S1 = Member("Yoon SeoYeon", "S1", "21", "August 6 2003", "Dodger Blue")
# S1.gnd_Part("dashi haeboja")

#--------------------------------------------------------------------------#

# --- INHERITANCE --- #
# INHERIT ATTRIBUTES FROM PARENT CLASS
# soosein = NPC()
# seoyeon = idol()
# soosein.yap()
# seoyeon.sing()

# MULTILEVEL INHERITANCE
# naky = tripleS()
# naky.objekt()

# MULTIPLE INHERITANCE
# A child can inherit more than 1 parent attributes
# hyuna = hyuna()
# hyuna.loser()

# METHOD CHAINING
# chaining more than 1 method
# MUST return self at the end of every method functions
# naky.objekt().blabla()

#--------------------------------------------------------------------------#

# --- SUPER FUNCTIONS --- #
# Function used to give access to the methods of parent class.
# Returns a temporary object of a parent class when used
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        return self.length * self.width
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

sqr = Square(5, 5)
cube = Cube(5, 5, 5)
# print(sqr.area())
# print(cube.volume())

#--------------------------------------------------------------------------#

# --- ABSTRACT CLASSES --- #
# prevents a user from creating an object of that class
# compels user to override abstract methods in a child class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod # CHILDREN OF THIS CLASS MUST OVERWRITE THIS ABSTRACT METHOD
    def go(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You are driving the car")
class Motorcycle(Vehicle):
    def go(self):
        print("You are riding the motorcycle")
car = Car()
motorcycle = Motorcycle()
# car.go()
# motorcycle.go()

#--------------------------------------------------------------------------#

# --= DUCK TYPING --- #
# Concept where the class of an object is less important than the methods/attributes
# Class type is not checked if minimum methods/attributes are present
# " IF IT WALKS LIKE A DUCK, AND QUACKS LIKE A DUCK, THEN IT MUST BE A DUCK! "
# " IF IT SINGS LIKE A S, AND DANCES LIKE A S, THEN IT MUST BE A S!"
class NaKyoung:
    def line(self):
        print("kkume nanido jom deo nan nopilge")
    def dancePart(self):
        print("NaKyoung's stretch")
class YooYeon:
    def line(self):
        print("dashi haebolkka")
    def dancePart(self):
        print("YooYoen's bow and arrow")
class girlsNeverDie:
    def part(self, nakyoung):
        nakyoung.line()
        nakyoung.dancePart()
        print("You are a tripleS member!")
# nakyoung = NaKyoung()
# yooyeon = YooYeon()
# girlsneverdie = girlsNeverDie()
# girlsneverdie.part(yooyeon)

#--------------------------------------------------------------------------#

# --- WALRUS OPERATOR --- #
# assigns values to a variable as part of a larger expression
SNames = list()
# while SName := input("Add your favorite S's: ") != 'quit':
#     SNames.append(SName)
# generally shortens the entire program

#--------------------------------------------------------------------------#

# --- HIGHER ORDER FUNCTION --- #
# A function that is either returning a function, OR accept a function as an argument
def cap(text):
    return text.upper()
def low(text):
    return text.lower()
def hello(func):
    text = func("hello")
    print(text)

# hello(cap)

#--------------------------------------------------------------------------#

# --- LAMBDA FUNCTION --- #
# function written in 1 line using lambda keyword accepts any number of arguments but only has one 
# expression (shortcut)
# Syntax -> lambda parameters:expression
triple = lambda x:x * 3
age_check = lambda age: True if age >= 18 else False
# print(triple(5))
# print(age_check(18))

#--------------------------------------------------------------------------#

# --- SORTING --- #
# sort() method = used with lists
# sort() function = used with iterables such as tuple
uriMemberList = ["SeoYeon", "Hyerin", "Jiwoo", "Chaeyeon", "YooYeon"]
uriMemberTuple = ("SeoYeon", "Hyerin", "Jiwoo", "Chaeyeon", "YooYeon")
uriMemberList.sort()
uriMemberTuple = sorted(uriMemberTuple)
# for i in uriMemberList:
#     print(i)
# for i in uriMemberTuple:
#     print(i)

# NEXT LEVEl
uriMember = [("SeoYeon", "S1", 21), 
             ("YeonJi", "S12", 16), 
             ("NaKyoung", "S7", 21),
             ("YooYeon", "S5", 23),
             ("HaYeon", "S19", 17)]
SNum = lambda num:int(num[1][1:])
uriMember.sort(key=SNum)
# for i in uriMember:
#     print(i)

#--------------------------------------------------------------------------#

# --- MAP --- #
# map() = applies a  function to each item in an iterable (list, tuple, etc)
# map(function, iterable)

store = [("The Story Begins", 60.00),
         ("Assemble24", 25.00),
         ("How Sweet", 30.00)]
to_rupiah = lambda data: (data[0], data[1]*15435.60)
idr_price = list(map(to_rupiah, store))
# for i in idr_price:
#     print(i)

#--------------------------------------------------------------------------#

# --- FILTER --- #
# filter() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

drinking_age = lambda data: data[2] >= 19
drinking_member = list(filter(drinking_age, uriMember))
# for i in drinking_member:
#     print(i)

# --- REDUCE --- #
# reduce() applies a function to the first two elements and repeat until 1 value remain
# DONT FORGET TO import functools!!!
import functools
factorial = [6,5,4,3,2,1]
res = functools.reduce(lambda x,y:x*y, factorial)
# print(res)

#--------------------------------------------------------------------------#

# --- LIST COMPREHENSION --- #
# A way to create a new list with less lines of codes and easier to read than lambda
# list = [expression for i in iterable if conditional (optional)]
# list = [expression if/else for i in iterable]
squares = []
for i in range(1,11):
    squares.append(i * i)
# print(squares)
# with List Comp:
squares = [i * i for i in range(1,11)]
# print(squares)
# Mimic a lambda function
grades = [100, 90, 81, 73, 40, 52, 60, 62, 31, 0]
# passed_stud = list(filter(lambda x: x >= 60, grades))
# print(passed_stud)
# with List Comp
passed_stud = [i for i in grades if i >= 60]
# with else
passed_stud = [i if i >= 60 else "FAILED" for i in grades]
# print(passed_stud)

#--------------------------------------------------------------------------#

# --- DICTIONARY COMPREHENSION --- #
# Same as list comp

# dictionary = {key: expression for (key,value) in iterable}
cities_in_F = {'NY': 32, 'Boston': 75, 'LA': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# dictionary = {key: expression for (key,value) in iterable if conditional}
member_month = {'NaKyoung': "October", 'SeoYeon':"August", 'SoHyun': "October", 'HaYeon':"August"}
oct_mem = {key: value for (key,value) in member_month.items() if value == "October"}
# print(oct_mem)
aug_mem = {key: value for (key,value) in member_month.items() if value == "August"}
# print(aug_mem)

# dictionary = {key: (if/else) for (key,value) in iterable}
mem_zodiac = {key: ("LIBRA" if value == "October" else "LEO") for (key,value) in member_month.items()}
# print(mem_zodiac)

# dictionary = {key: function(value) for (key,value) in iterable}
def zodiac_Check(value):
    if(value == "October"):
        return "LIBRA"
    else:
        return "LEO"
mem_zodiac2 = {key: zodiac_Check(value) for (key,value) in member_month.items()}
# print(mem_zodiac2)

#--------------------------------------------------------------------------#

# --- ZIP FUNCTION --- #
# zip(*iterables) aggregate atau menyatukan two or more iterables (list, tuples, sets, etc)
# Creates a zip object with paired elements
toripuruesu = ["SeoYeon", "Hyerin", "Jiwoo"]
esunamba = ["S1", "S2", "S3"]
tripleesu = zip(toripuruesu, esunamba)
# for i in tripleesu:
#     print(i) 
# Zips can also be cast into a dictionary or other form of iterables
tripleesu = dict(zip(toripuruesu, esunamba))
# for key,value in tripleesu.items():
#     print(key + " : " + value)

#--------------------------------------------------------------------------#

# --- TIME (THE WORLD) --- #
# don't forget to import time

# print(time.ctime(0)) # ctime converts a time expressed in seconds since epoch to a readable string
                       # EPOCH is when my computer thinks time began (ref point)

# print(time.time()) # return current seconds since epoch

# print(time.ctime(time.time())) # return current seconds since epoch in a readable string of date and time
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time.strptime(time_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

#--------------------------------------------------------------------------#

# --- MULTITHREADING --- #
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading
# Dont forget to import time and threading
import threading
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You finish studying")

# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
# z = threading.Thread(target=study, args=())
# z.start()
# Joins the threads to wait for the rest to follow up
# x.join()
# y.join()
# z.join()

# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

#--------------------------------------------------------------------------#

# --- DAEMON THREADS --- #
# daemon thread = a thread that runs in the background, not important for program to run
#                 the program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, it stays alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes
# don't forget to import time and threading

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
# x.start()

# x.setDaemon(True)
# print(x.isDaemon())

# answer = input("Do you wish to exit?")

#--------------------------------------------------------------------------#

# --- MULTIPROCESSING --- #
# Multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

# def main():

#     print("cpu count:", cpu_count())

#     start_time = time.perf_counter()

#     a = Process(target=counter, args=(500000000,))
#     b = Process(target=counter, args=(500000000,))

#     a.start()
#     b.start()

#     print("processing...")

#     a.join()
#     b.join()

#     end_time = time.perf_counter()

#     print("Done!")
#     elapsed_time = end_time - start_time
#     print(f"finished in: {elapsed_time} seconds")


# if __name__ == '__main__':
#     main()

#--------------------------------------------------------------------------#

# --- GUI STUFF --- #
# Graphical User Interface to display the program in a neat window
# Widgets = different elements in a UI such as buttons, textbox, images, etc
# Window = a container to store the widgets and display them
# use TKINTER 

from tkinter import *
from PIL import Image, ImageTk

# THE BASIC
# =========
# window = Tk() # instantiate an instance of a window
# window.geometry("420x420") # change the size of the window
# window.title("First Window!") # change the title of the program on top

# icon = PhotoImage(file='...') # change a image file to PhotoImage
# window.iconphoto(True,icon) # change the window icon to the icon you want
# window.config(background='black') # change the background color

# window.mainloop() # place window on the screen, also listens for events

# LABELS
# =========
# Label is an area widget that holds text and/or an image inside a window
# window = Tk()
# photo = PhotoImage(file='C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\soyon.png')
# label = Label(window, 
#               text="Hey!", 
#               font=('Arial', 40, 'bold'), 
#               fg='black', 
#               relief=RAISED, 
#               bd=10, 
#               padx=20, 
#               pady=20,
#               image=photo,
#               compound='bottom')
# label.pack()
# window.mainloop()

# BUTTONS
# =========
# Buttons is a clickable element that will do stuff
# def click():
#     print("You clicked on chaewon!")

# window = Tk()
# img = Image.open('C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\PyProjects\\images\\Screenshot (1202).png')
# resized = img.resize((500,400))
# chewon = ImageTk.PhotoImage(resized)
# button = Button(window, 
#                 text = 'Click Chaewon!',
#                 font=('Arial', 40, 'bold'),
#                 command=click,
#                 fg='white',
#                 bg='black',
#                 image=chewon,
#                 compound='bottom',
#                 relief=RAISED,
#                 bd=10,
#                 padx=20,
#                 pady=20)
# button.pack()
# window.mainloop()

# ENTRYBOX
# =========
# Entry widget = textbox that a acc a single line of input
# def submit():
#     usrname = entry.get()
#     print(f"Hello {usrname}")
# def erase():
#     entry.delete(0,END)
# def backspace():
#     entry.delete(len(entry.get())-1, END)

# window = Tk()
# entry = Entry(window,
#               font=("Arial", 40))
# entry.pack(side=LEFT)
# submit_button = Button(window,
#                        text="Submit",
#                        command=submit,
#                        padx=10,
#                        pady=10,
#                        font=('Arial', 20))
# delete_button = Button(window,
#                        text="Delete",
#                        command=erase,
#                        padx=10,
#                        pady=10,
#                        font=('Arial', 20))
# backspace_button = Button(window,
#                        text="Backspace",
#                        command=backspace,
#                        padx=10,
#                        pady=10,
#                        font=('Arial', 20))
# entry.config(show='*') # Password related
# submit_button.pack(side=RIGHT)
# delete_button.pack(side=RIGHT)
# backspace_button.pack(side=RIGHT)
# window.mainloop()

# CHECKBOX
# =========

# def display():
#     if(x.get()==1):
#         print("You agree!")
#     else:
#         print("You don't agree :(")

# window = Tk()

# x = IntVar()

# soyon_photo = PhotoImage(file='C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\soyon.png')

# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=soyon_photo,
#                            compound='left')
# check_button.pack()
# window.mainloop()

# RADIO BUTTONS
# =========

sss = ["SeoYeon","NaKyoung","YooYeon"]

def order():
    if(x.get()==0):
        print("You chose SeoYeon!")
    elif(x.get()==1):
        print("You chose NaKyoung!")
    elif(x.get()==2):
        print("You chose YooYeon!")
    else:
        print("You picked no one")

window = Tk()

syImage = PhotoImage(file='C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\seoyeon.png')
nyImage = PhotoImage(file='C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\nakyoung.png')
yyImage = PhotoImage(file='C:\\Users\\Asus VivobookPro\\Documents\\CODING STUFF\\PYTHON STUFF\\PY\\Studee\\yooyeon.png')
sssImages = [syImage,nyImage,yyImage]

x = IntVar()

for index in range(len(sss)):
    radiobutton = Radiobutton(window,
                              text=sss[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx = 25, #adds padding on x-axis
                              font=("Arial",50),
                              image = sssImages[index], #adds image to radiobutton
                              compound = 'left', #adds image & text (left-side)
                              indicatoron=0, #eliminate circle indicators
                              width = 500, #sets width of radio buttons
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)
window.mainloop()

# SCALE
# =========

# LISTBOX
# =========

# MESSAGEBOX
# =========

# COLOR CHOOSER
# =========

# TEXT AREA
# =========

# OPEN A FILE
# =========

# SAVE A FILE
# =========