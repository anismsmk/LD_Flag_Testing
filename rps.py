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
        print("Tie :/")
    if(computer == "Scissors" and (player == "Paper" or player == "Lizard")):
        print("BAZINGA!")
    elif(computer == "Lizard" and (player == "Paper" or player == "Spock")):
        print("BAZINGA!")
    elif(computer == "Spock" and (player == "Rock" or player == "Scissors")):
        print("BAZINGA!")
    elif(computer == "Paper" and (player == "Rock" or player == "Spock")):
        print("BAZINGA!")
    elif(computer == "Rock" and (player == "Scissors" or player == "Lizard")):
        print("BAZINGA!")
    elif(player == "Scissors" and (computer == "Paper" or computer == "Lizard")):
        print("YOU LOSE!")
    elif(player == "Lizard" and (computer == "Paper" or computer == "Spock")):
        print("YOU LOSE!")
    elif(player == "Spock" and (computer == "Rock" or computer == "Scissors")):
        print("YOU LOSE!")
    elif(player == "Paper" and (computer == "Rock" or computer == "Spock")):
        print("YOU LOSE!")
    elif(player == "Rock" and (computer == "sSissors" or computer == "Lizard")):
        print("YOU LOSE!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = T[randint(0,4)]
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