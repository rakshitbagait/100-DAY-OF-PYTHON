
print("welcome to the calculator")
print(
    '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|            _            _       _             
                    | |          | |     | |            
            ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
            / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
            | (_| (_| | | (__| |_| | | (_| | || (_) | |   
            \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                ''')
def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 

def calculator():
  num1= float(input("Enter the first number"))
  num2 = float(input("enter the second number"))
  operation={"Addition":"A",
             "Subtraction":"S",
             "Multiplication":"M",
             "Division":"D"}
  print(operation)
  choice = input("enter the choice").lower()

  if choice=="a":
    print(add(num1,num2))
  elif choice =="s":
    print(subtract(num1,num2))
  elif choice == "m":
    print(multiply(num2,num2))
  elif choice == "d":
    print(divide(num1,num2))
  else:
    print("Enter a valid choice")
    calculator()
  
  choice = input("Do you want to continue Yes or No").lower()

  if choice == "yes":
    calculator()
  else:
    print("Thank you")
    return 
calculator()

    
      