import random as rd

# random_integer = rd.randint(a=1, b= 10000000)
# print(random_integer)

# print(rd.random())
# random_integer = rd.uniform (a=1, b= 10000000)
# print(random_integer)

random_toss = rd.randint(a=0,b=1)

if random_toss == 0:
    print("Heads")
else:
    print("tails")
