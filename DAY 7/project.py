import random 

words = [
    "apple", "banana", "ocean", "guitar", "pencil", "mountain", "elephant", "galaxy",
    "horizon", "jungle", "parrot", "volcano", "whisper", "zigzag", "sunflower", "pyramid",
    "raindrop", "notebook", "lantern", "treasure"
]
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    =======
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\ 
       |
    =======
    """
]

lives = 0
# index= hangman_stages[0]



random_word = random.choice(words)
print(random_word)
length_of_random_word= len(random_word)
print(length_of_random_word)


for i in range(0,length_of_random_word):
    print("_",end=" ")
a=True

correct_letter=[]
while a:
    user_guess = input("\nguess a letter from the word").lower()
    display=""
    for letter in random_word:
        if letter == user_guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
            
        else:
            display += "_"
    
        
    print("\n",display)

    if user_guess not in random_word:
        lives +=1
        if lives ==6:
            a=False
            print("Game over! you killed him!!")
            print(f"The correct word was {random_word}")
    if "_" not in display:
        print("You win")
        a = False
    print(hangman_stages[lives])



    