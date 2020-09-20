import sys

s = sys.argv
try:
    num1 = open(s[1])
    num2 = num1.read()
    num3 = num2.strip()
    num4 = num3.split()
    for i in num4:
        print(i)
finally:
    num1.close()
