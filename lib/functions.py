#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return(num1 + num2)



def halve(number):
    if type(number) == int or type(number) == float:
        return number / 2
    return None

