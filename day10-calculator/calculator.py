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


if __name__ == '__main__':
    print(logo)
    operations = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide,
    }

    num1 = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from a line above: ")
    num2 = int(input("What's the second number? "))
    
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
