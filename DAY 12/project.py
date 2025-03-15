import random

ascii_art = """

   _____                       _   _                 _               
  / ____|                     | \ | |               | |              
 | |  __ _   _  ___  ___ ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                     
                                                                     
  
                             
"""
print(ascii_art)

print("welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
difficulty =input("Choose a difficulty 'easy' or 'hard' ").lower()
choosed_number = random.randint(1,100)
def numberGuesser(difficulty,choosed_number):

    if difficulty =="easy":
        a=0
        for i in range(10,0,-1):
            print(f"You have {i} attempts remaining to guess the number")
            choice = int(input("make a choice"))
            if choice == choosed_number:
                print("you are right!!")
                a=1
                break
            elif choice>choosed_number:
                print("Too high")
            elif choice < choosed_number:
                print("Too low")
            else:
                print("make a choice beween 1 and 100 ")
        if a==0:
            print(f"the number was {choosed_number}. You Loose")
    elif difficulty == "hard":
        a=0
        for i in range(5,0,-1):
            print(f"yout have {i} attempts remaining to guess the number")
            choice = int(input("make a choice"))
            if choice == choosed_number:
                print("you are right!!")
                a=1
                break
            elif choice>choosed_number:
                print("Too high")
            elif choice < choosed_number:
                print("Too low")
            else:
                print("make a choice beween 1 and 100 ")
        if a==0:
            print(f"the number was {choosed_number}. You Loose")

numberGuesser(difficulty,choosed_number)