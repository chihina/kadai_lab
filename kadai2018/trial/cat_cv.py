# this is a program to read a file
chihiro = open("cv000_29590.txt")
s = chihiro.read()
try:
    print(s)
finally:
    chihiro.close()
