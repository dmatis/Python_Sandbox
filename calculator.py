from sys import argv
#A simple program to perform math operations

script, a, b = argv
valueA = int(a)
valueB = int(b)


def divide(a, b):
    print "%d / %d = " % (a,b),
    return a / b

def add(a, b):
    print "%d + %d = " % (a,b),
    return a+b

def subtract(a, b):
    print "%d - %d = " % (a,b),
    return a-b

def multiply(a, b):
    print "%d * %d = " % (a,b),
    return a*b

print "Please specify math operation (/ + - *):"
math_op = raw_input()

if (math_op == '/'):
    print divide(valueA, valueB)
if (math_op == '+'):
    print add(valueA, valueB)
if (math_op == '-'):
    print subtract(valueA, valueB)
if (math_op == '*'):
    print multiply(valueA, valueB)
