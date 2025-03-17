import random
import os 

from data import instagram_accounts

def assign():
    person = random.choice(instagram_accounts)
    return person

def print_person(p1, p2):
    print(f"compare A: {p1['username']}, a {p1['profession']}, from {p1['country']}")
    print(f"Against B: {p2['username']}, a {p2['profession']}, from {p2['country']}")

def compare(choice, sum1, sum2, p1, p2):
    global score, game_on
    if sum1 > sum2:
        max_followers = sum1
    else:
        max_followers = sum2
    
    if choice == 'a':
        answer = sum1
    elif choice == 'b':
        answer = sum2
    else:
        game_on = False
        return p1, p2
    
    if answer == max_followers:
        p1 = p2
        p2 = assign()
        score += 1
        game_on = True
    else:
        game_on = False
    
    return p1, p2

def higher_lower_game():
    global game_on, p1, p2, score
    p1 = assign()
    p2 = assign()
    while p1 == p2:
        p2 = assign()
    
    game_on = True
    score = 0
    
    while game_on:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
  _    _ _       _                
 | |  | (_)     | |               
 | |__| |_  __ _| |__   ___ _ __  
 |  __  | |/ _` | '_ \ / _ \ '__| 
 | |  | | | (_| | | | |  __/ |    
 |_|  |_|_|\__, |_| |_|\___|_|    
 | |        __/ |                 
 | |     __|___/    _____ _ __    
 | |    / _ \ \ /\ / / _ \ '__|   
 | |___| (_) \ V  V /  __/ |      
 |______\___/ \_/\_/ \___|_|      
                                                   
""")
        
        print_person(p1, p2)
        choice = input("Who has more followers? Type 'A' or 'B':").lower()
        sum1 = p1["followers_millions"]
        sum2 = p2["followers_millions"]
        
        p1, p2 = compare(choice, sum1, sum2, p1, p2)
    
    print(f"OOps! Its a wrong answer❌. Your score is {score}")

higher_lower_game()
