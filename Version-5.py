import random as rd

guesses_made = []
counter = 5
magic_number = rd.randint(1, 100)
print(magic_number)
lower_higher = []

guess = int(input("Guess a number between 1 and 100: "))

while guess != magic_number and counter > 0:
  if guess < magic_number:
    print("Your guess is too low!")
  elif guess > magic_number:
    print("Your guess is too high!")
    
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
    guess = int(input("Guess Again: "))
else:
  print("You Win!")
