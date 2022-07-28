from random import randint

def rps():

  #### VARIATION NORMAL ####
  #create a list of play options
  t = ["Rock", "Paper", "Scissors"]
  
  #assign a random play to the computer
  computer = t[randint(0,2)]
  
  #set player to False
  player = False
  
  while player == False:
  #set player to True
      player = input("Rock, Paper, Scissors?\n")
      if player == computer:
          print("Tie!")
      elif player == "Rock":
          if computer == "Paper":
              print("You lose!", computer, "covers", player)
          else:
              print("You win!", player, "smashes", computer)
      elif player == "Paper":
          if computer == "Scissors":
              print("You lose!", computer, "cut", player)
          else:
              print("You win!", player, "covers", computer)
      elif player == "Scissors":
          if computer == "Rock":
              print("You lose...", computer, "smashes", player)
          else:
              print("You win!", player, "cut", computer)
      else:
          print("That's not a valid play. Check your spelling!")
      #player was set to True, but we want it to be False so the loop continues
      player = False
      computer = t[randint(0,2)]
    #### END OF VARIATION NORMAL ####

    #### VARIATION CRAZY ####

def rps_crazy():

  T = ["Rock", "Paper", "Scissors", "Lizard", "Spok"]
  #assign a random play to the computer
  computer = T[randint(0,4)]
  print(computer)
  #set player to False

  player = False
  
  while player == False:
    player = input("Rock, Paper, Scissors, Lizard, Spock?\n")
    if player == computer:
        print("Again!")
    if(computer == "scissors" and (player == "paper" or player == "lizard")):
        Win = True
    elif(computer == "lizard" and (player == "paper" or player == "Spock")):
        Win = True
    elif(computer == "Spock" and (player == "rock" or player == "scissors")):
        Win = True
    elif(computer == "paper" and (player == "rock" or player == "Spock")):
        Win = True
    elif(computer == "rock" and (player == "scissors" or player == "lizard")):
        Win = True
    elif(player == "scissors" and (computer == "paper" or computer == "lizard")):
        Lose = True
    elif(player == "lizard" and (computer == "paper" or computer == "Spock")):
        Lose = True
    elif(player == "Spock" and (computer == "rock" or computer == "scissors")):
        Lose = True
    elif(player == "paper" and (computer == "rock" or computer == "Spock")):
        Lose = True
    elif(player == "rock" and (computer == "scissors" or computer == "lizard")):
        Lose = True

                # Scissors cuts Paper  

                # Paper covers Rock   

                # Rock crushes Lizard   

                # Lizard poisons Spock   

                # Spock smashes Scissors   

                # Scissors decapitates Lizard   

                # Lizard eats Paper   

                # Paper disproves Spock   

                # Spock vaporizes Rock   

                # (and as it always has) Rock crushes Scissors   

    #### END OFVARIATION CRAZY ####