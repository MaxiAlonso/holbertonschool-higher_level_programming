#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
argc = len(argv) - 1
operators = ["+", "-", "*", "/"]
if argc != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif argv[2] in operators:
    if argv[2] == "+":
        result = add(int(argv[1]), int(argv[3]))
    elif argv[2] == "-":
        result = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == "*":
        result = mul(int(argv[1]), int(argv[3]))
    elif argv[2] == "/":
        result = div(int(argv[1]), int(argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {result}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
