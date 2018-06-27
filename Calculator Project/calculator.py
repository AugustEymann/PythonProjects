# This is my first python program
# It could be more efficient using loops etc.

import sys

def add(num, num1):
    return num + num1


def sub(num, num1):
    return num - num1


def mult(num, num1):
    return num * num1 


def div(num, num1):
    return num / num1


exit = False
while (exit == False):
    userinput = input("What would you like to do?\n")
    if ("add" in userinput.lower()):
        numb1 = int(input("Provide me one number that you would like to add\n"))
        numb2 = int(input("Provide me another number that you would like to add\n"))
        print("Your result is:",add(numb1, numb2))
    elif ("sub" in userinput.lower()):
        numb1 = int(input("Provide me one number that you would like to subtract\n"))
        numb2 = int(input("Provide me another number that you would like to subtract\n"))
        print("Your result is:",sub(numb1, numb2))
    elif ("mult" in userinput.lower()):
        numb1 = int(input("Provide me one number that you would like to multiply\n"))
        numb2 = int(input("Provide me another number that you would like to multiply\n"))
        print("Your result is:",mult(numb1, numb2))
    elif ("div" in userinput.lower()):
        numb1 = int(input("Provide me one number that you would like to divide\n"))
        numb2 = int(input("Provide me another number that you would like to divide\n"))
        print("Your result is:",div(numb1, numb2))
    check = input("You'd you like to exit?\n")
    if ("y" in check.lower()):
        exit = True
