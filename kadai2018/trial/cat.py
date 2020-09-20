# this is a file to study command line subject
import sys

s = sys.argv
chihiro = open(s[1])
s = chihiro.read()
try:
    print(s)
finally:
    chihiro.close()
