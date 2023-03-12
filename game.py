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
type = input("OPERATION OF +-/*:")
time.sleep(1)
print("RULES:")
time.sleep(1)
if type == "+":
  print("ADD 1 TO THE NUMBER WE GIVE YOU")
elif type == "-":
  print("SUPTRACT 1 TO THE NUMBER WE GIVE YOU") 
elif type == "*":
  print("MULTIPLY 2 TO THE NUMBER WE GIVE YOU") 
elif type == "/":
  print("DIVIDE 2 TO THE NUMBER WE GIVE YOU") 
time.sleep(1)
print("STARTING...!")
time.sleep(5)
num = 0
while True:
  a = int(input(num))
  if type == "+":
    if a == num + 1:
        num = a + 1
  elif type == "-":
    if a == num - 1:
        num = a - 1
  elif type == "*":
    if a == num * 2:
        num = a * 2 
  elif type == "/":
    if a == num / 2:
        num = a / 2
  time.sleep(1)
