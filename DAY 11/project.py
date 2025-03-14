import random
def BlackJack():
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]


    your_card_1= random.choice(cards)
    your_card_2 = random.choice(cards)
    your_cards = [your_card_1,your_card_2]
    your_total = your_card_1+your_card_2

    computer_card_1 = random.choice(cards)
    computer_cards =[computer_card_1]
    computer_total =computer_card_1
    print(f"your cards: {your_cards} your score: {your_total}")
    print(f"Computer first card {computer_cards}")
    choice = input("Type 'y' to get another card, type 'n' to pass ").lower()
    if choice =='y':
        your_card_3 = random.choice(cards)
        your_cards.append(your_card_3)
        your_total += your_card_3
        computer_card_2 = random.choice(cards)
        computer_cards.append(computer_card_2)
        computer_total+= computer_card_2

        print(f"your cards: {your_cards} your score: {your_total}")
        print(f"computer final hand :{computer_cards} computers score {computer_total}")
        
        if your_total<=21 and your_total>computer_total:
            print("You Win")
        elif your_total==computer_total:
            print("It is draw")
        
        else:
            print("Your loose")
    elif choice=='n':
        if your_total<=21 and your_total>computer_total:
            print("You Win")
        elif your_total==computer_total:
            print("It is draw")
        else:
            print("Your loose")
    else :
        print("enter a right choice")
        BlackJack()
            
    choice2 = input("Do you want to play'y' or 'n'").lower()
    if choice2== "y":
        BlackJack()
    else:
        return 0

        
BlackJack()
