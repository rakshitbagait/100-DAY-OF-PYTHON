import random

scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''

computer_rock = '''
      ,--.--._
------" _, \\___)
        / _/____)
        \\//(____)
------\\     (__) 
       `-----"
'''

player_rock = '''
      __.--.--,      
     (___/ , _ "------  
      (____\\ _ \\      
       (____)\\\\/
        (__)     /------  
         "-----'  
'''

paper = '''
          _.-._
        | | | |_
        | | | | |
        | | | | |
      _ |  '-._ |
      \\`\\`-.'-._;
       \\    '   |
        \\  .`  /
        |    |
'''

# Start game
print("Let's play Rock, Paper, Scissors!")

computer_choice = random.randint(0, 2)
players_choice = int(input("What is your choice? (0: Rock, 1: Paper, 2: Scissors): "))

# Display choices
if players_choice == 0:
    print("You chose Rock:")
    print(player_rock)
elif players_choice == 1:
    print("You chose Paper:")
    print(paper)
elif players_choice == 2:
    print("You chose Scissors:")
    print(scissors)
else:
    print("Invalid choice! Please choose 0, 1, or 2.")
    exit()

if computer_choice == 0:
    print("Computer chose Rock:")
    print(computer_rock)
elif computer_choice == 1:
    print("Computer chose Paper:")
    print(paper)
elif computer_choice == 2:
    print("Computer chose Scissors:")
    print(scissors)

# Game logic
if players_choice == computer_choice:
    print("It's a draw!")
elif (players_choice == 0 and computer_choice == 2) or \
     (players_choice == 1 and computer_choice == 0) or \
     (players_choice == 2 and computer_choice == 1):
    print("You win! 🎉")
else:
    print("You lose! 😢")
