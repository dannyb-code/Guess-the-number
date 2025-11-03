import random as rd

guesses_made = []
counter = 3
magic_number = rd.randint(1, 10)
#print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))

while guess != magic_number and counter > 0:
  counter -= 1
  guesses_made.append(guess)
  print("Incorrect!")
  print("%s guesses remain." % (counter))
  print(" ")
  if counter == 0:
    print("You Lose!")  
    break
  else:
    print("You have already guessed: %s" %  guesses_made)
    gues = int(input("Guess Again"))

else:
  print("You Win!")
