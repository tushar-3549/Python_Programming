import random
while True:
    ch = ["Rock","Paper","Scissors"]
    com = random.choice(ch)
    player = None
    
    while player not in ch:
        player = input("Rock , Paper or Scissors : ")
        
    if player == com:
        print("Computer : ",com)
        print("Player : ",player)
        print("Game Tie !")
    elif player == "Rock":
        if com == "Paper":
            print("Computer : ",com)
            print("Player : ",player)
            print("You Lose !")
        if com == "Scissors":
            print("Computer : ",com)
            print("Player : ",player)
            print("You Win !")
    elif player == "Scissors":
       if com == "Rock":
           print("Computer : ",com)
           print("Player : ",player)
           print("You Lose !")
       if com == "Paper":
           print("Computer : ",com)
           print("Player : ",player)
           print("You Win !")
    elif player == "Paper":
       if com == "Scissors":
           print("Computer : ",com)
           print("Player : ",player)
           print("You Lose !")
       if com == "Rock":
           print("Computer : ",com)
           print("Player : ",player)
           print("You Win !")
    play_again = input("Want to play again : (Y/N) : ")
    if play_again != 'Y':
      break
print("Bye !")
         
        
