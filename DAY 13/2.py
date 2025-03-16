try :
    age = int(input("How old are you?"))


except ValueError:
    print("you have type in an invalid number")
    age = int(input("Enter your age"))


if age >=18:
    print(f"you can drive at age{age}")

