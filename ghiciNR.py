import os
os.system('cls')
# generate random integer values
from random import seed
from random import randint
# generate some integers
for _ in range(1):
	value = randint(1, 100)
	print("\n\t",value)
#*************************************************************
x=int(input("\n Introduceti un numar intre 1 si 100: "))
1<=x<=100
#print("\n Numarul trebuie sa fie in intervalul 1 - 100 !!!\n")
while value!=x:
    if value<x:
        print("\n\tPrea MARE!")
        x=int(input(" Introduceti un numar: "))
    elif value>x:
        print("\n\tPrea MIC!")
        x=int(input(" Introduceti un numar: "))
os.system('cls')
print("\n\n\tAi ghicit !!!\n")
print("\tNumarul generat este:",value)
print("\n\n\n")