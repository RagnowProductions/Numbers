import math
import time
print("A FENNGAMING ORIGINAL")
time.sleep(1)
print("FINALLY MADE IN PYTHON INSTEAD OF SCRATCH")
time.sleep(3)
print("FENNGAMING NUMBERS GAME.PYTHON")
time.sleep(1)
print("PRODUCED BY RAGNOWPRODUCTIONS 2023")
time.sleep(1)
print("RULES: TYPE THE NUMBER AFTER THE VARIABLE BEFORE (WE'LL GIVE YOU A NUMBER AND YOU HAVE TO ADD 1) ")
time.sleep(1)
print("STARTING...!")
time.sleep(5)
num = 0
while True:
    a = int(input(num))
    if a == num + 1:
        num = a + 1
    elif a == num - 1:
        print("ERR: IT'S ADDITION, NOT SUBTRACTION")
    elif a == num * 2:
        print("ERR: IT'S ADDITION, NOT MULTIPLICATION")
    elif a == num / 2:
        print("ERR: IT'S ADDITION, NOT DIVISION")
    elif a > num + 2:
        print("ERR: INTEGER TOO BIG")
    elif a < num:
        print("ERR: INTEGER TOO SMALL")
    elif a == num + 2:
        print("ERR: IT'S ADDITION, NOT ADDITION")
    elif a == num:
        print("ERR: THAT'S THE NUMBER WE GAVE YOU")
    elif a == 3.14159:
        print("PI, YOU SAY? WELL, OK! " + math.pi)
    time.sleep(1)