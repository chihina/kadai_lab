# this is a file to study command line subject
import sys

s = sys.argv
num1 = open(s[1])
p = num1.read()
try:
    num2 = open(s[2], mode = "w")
    num2.write(p)
    num2.close
finally:
    num1.close()
