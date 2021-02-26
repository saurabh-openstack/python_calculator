import os
import click

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b


def displayChoice():
    print("************ Welcome to Calculator***********")
    print("Enter Choice")
    print("1. Add")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")

def getChoice():
    choice = 1
    while (True):
        choice = int(input("Enter Choice : "))
        if(choice <= 4 and choice >= 1):
            break
        else:
            print("Enter correct choice ")
    return choice

def displayChoosenChoice(choice):
    if (choice == 1):
        print("You choosen Addition ")
    elif (choice == 2):
        print("You choosen Substraction ")
    elif (choice == 3):
        print("You choosen Division ")
    elif (choice == 4):
        print("You choosen Multiplication ")


def getData():
    temp_dict = []
    temp_dict.append(int(input("Enter value of A : ")))
    temp_dict.append(int(input("Enter value of B : ")))
    return temp_dict

def calc(choice,value_input):
    if (choice == 1):
        return add(value_input[0],value_input[1])
    if (choice == 2):
        return sub(value_input[0],value_input[1])
    if (choice == 3):
        return div(value_input[0],value_input[1])
    if (choice == 4):
        return mul(value_input[0],value_input[1])

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def Main():
    while True:
        displayChoice()
        choice = getChoice()
        displayChoosenChoice(choice)
        input = []
        input = getData()
        result = calc(choice,input)
        print("Result is ",result)
        if click.confirm('Do you want more calculation?', default=True):
            screen_clear()
        else:
            break

if __name__=="__main__":
    Main()
