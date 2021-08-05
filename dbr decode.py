#! /usr/bin/python

# import re
# import random

# def repl_fun(match):
#    return str(random.randint(0,9))

code = input("Enter the coded message: ")

for i in range(len(code)):
    code=str(chr(ord(code[i]) - 1))
    replaced = re.sub("!", repl_fun, code)
    replaced1 = re.sub("{", repl_fun, replaced)
    print (replaced1, end=" ")