#!/usr/bin/env python3

def Intro():
    print('Witaj w naszym prostym kalkulatorze!')
    print()
    
def WhatOperation():
    print('Wybierz jaką operacje chcesz wykonać')
    print('Dodawanie\t[+]')
    print('Odejmowanie\t[-]')
    print('Mnożenie\t[*]')
    print('Dzielenie\t[/]')

def GetFloat(message):
    while True:
        try:
            x = float(input(message))
            break
        except ValueError:
            print('To nie jest liczba. Spróbuj ponownie.')
            print()
    
    return x

def GetCorrectOperation():
    correctOperations = ['+', '-', '*', '/']
        
    while True:
        x = input()
        if x in correctOperations:
            break
        else:
            print('Nieprawidłowy znak. Spróbuj ponownie.')

    return x
    
def ChooseOperation():
    choice = GetCorrectOperation()
    
    x = GetFloat('Wprowadź pierwszą liczbę: ')

    y = GetFloat('Wprowadź drugą liczbę: ')

    if choice == '+':
        result = Addition(x, y)
    elif choice == '-':
        result = Substraction(x, y)
    elif choice == '*':
        result = Multiplication(x, y)
    elif choice == '/':
        result = Division(x, y)

    return result

def PrintResult(x):
    if x:
        print('Wynik to ', x)
    
def Addition(x, y):
    return x + y

def Substraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    return x / y

Intro()
WhatOperation()
PrintResult(ChooseOperation())
