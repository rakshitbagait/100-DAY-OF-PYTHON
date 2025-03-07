import random

friends=["alice","bob","charles","david","emaneul"]

print(random.choice(friends))

rand_index= random.randint(a=0,b=4)
print(friends[rand_index])

print(friends[::-1])

friends[-1]="mellons"
print(friends)
