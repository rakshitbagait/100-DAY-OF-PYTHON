# is prime

# is prime


def is_prime(num):
    a=0
    if num < 2:
        print("Neither prime nor composite")
        return
    if num == 2:
        print("prime")
        return
    if num>2:
      for i in range(2,num):
          if num%i ==0:
              a= 1
              break
    if a==1:
        print("composite")
        return
    
    else:
        print("prime")
        return

is_prime(73)