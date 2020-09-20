# this is a file to study command line subject
import sys

s = sys.argv
try:
    num1 = open(s[1])
    p = num1.read()
    num2 = p.split(".")
    for i in num2:
        t = i.split()
        for n in t:
            if n == s([2]):
                print(num2)
finally:
    num1.close()
