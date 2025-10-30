import random as rd

magic_number = rd.randint(1, 10)
#print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))
counter = 3

while guess != magic_number and counter > 0:
  counter = counter - 1
  print("You Lose!")
  counter_string = str(counter)
  print(counter_string + " guesses remain.")
  print(" ")
  if counter == 0:
    break
  guess = int(input("Guess a number between 1 and 10: "))

else:
  print("You Win!")
