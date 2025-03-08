# password generator
import random

# List of all uppercase and lowercase alphabets
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# List of numbers (0-9)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of common special characters
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '[', '{', ']', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', 
    '\\', '|', '`', '~'
]

letterUp=int(input("How many capital letters do you want in your password"))
letterLow= int(input("How many lowercase letter do you want in you password"))
num = int(input("How many number do you want in your password"))
sChar = int(input("How many special characters do you want in your password"))
password=""
for i in range(0,letterUp):
    password += random.choice(alphabets)
for i in range(0,letterLow):
    password += random.choice(small_case)
for i in range(0,num):
    password+=random.choice(numbers)
for i in range(0,sChar):
    password += random.choice(special_characters)

print(password)

def scramble_string(input_string):
    char_list = list(input_string)
    random.shuffle(char_list)
    return "".join(char_list)

scrambled_words = scramble_string(password)
print(scrambled_words)

