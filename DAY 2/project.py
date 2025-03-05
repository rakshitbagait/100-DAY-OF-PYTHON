# Tip calculator

print("Welcome to the tip calculator")
bill=float(input("what was your total bill"))
tip = float(input("How much tip would you like to give?"))
people = int(input("how many people to split the bill "))
total = bill/7 *(1+tip/100)
print(f"Each person should pay: ${total}")