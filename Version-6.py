import random as rd
import os 

play = True
games_played = 0
games_won = 0

while play:
  guesses_made = []
  counter = 5
  magic_number = rd.randint(1, 100)
  #print(magic_number)

  guess = int(input("Guess a number between 1 and 100: "))
  os.system("clear")


  while guess != magic_number and counter > 0:
    counter -= 1
    guesses_made.append(guess)
    print("Incorrect.")
    if guess < magic_number:
      print("Your guess is too low!")
    else:
      print("Your guess is too high!")
    print("%s guesses remain." % (counter))
    print(" ")
    if counter == 0:
      print("You Lose!")  
      games_played += 1
      break
    else:
      print("You have already guessed: %s" %  guesses_made)
      guess = int(input("Guess Again: "))
      os.system("clear")

  else:
    print("You Win!")
    games_won += 1
    games_played += 1
  
  print("SCOREBORD")
  print("Games Won: %s" % (games_won))
  print("Games Played: %s" % (games_played))
  
  play = input("Would you like to play again? (y/n): ")
  os.system("clear")
  if play == "y":
    play = True
    counter = 5 
  else:
    play = False
