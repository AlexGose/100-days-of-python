#!/bin/env python3

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide,
    }

    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from a line above: ")
    num2 = float(input("What's the second number? "))

    done = False
    while not done:
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        more_message = f"type 'y' to continue calculating with {answer}, or type "
        more_message += "'n' to start a new calculation. "
        more = input(more_message)
        
        if more == 'y':
            num1 = answer
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number? "))
        else:
            calculator()


if __name__ == '__main__':
    print(logo)
    calculator()
