def add(*a):
    sum =0
    for i in a :
        sum +=i
    return sum

print(add(232,234,235423,23532,4525,5235,2523,52,3524235235252,5,235,325,325,32,532,5,25,325,32,523,5,2335,235,2,52,35,23,523,5,325,25,2,52,35,325,32,5,325,23,52,35,325,25,))


def calculate(**kwargs):
    print(kwargs)
calculate(add=23,value=45)