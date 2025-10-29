import random as rd

magic_number = rd.randint(1, 10)
#print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))

while guess != magic_number:
  print("You lose!")
  guess = int(input("Guess a number between 1 and 10: "))
else:
  print("You win!")
