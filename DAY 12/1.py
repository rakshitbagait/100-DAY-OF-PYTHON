enemies =1

def increase_enemies():
    enemies =2
    print(f"enemies inside the function {enemies}")
    def drink_potion():
        print("hey")
    drink_potion()
increase_enemies()
print(f"enemies outside fucntion : {enemies}")

