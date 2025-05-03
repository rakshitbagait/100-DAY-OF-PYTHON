# list comprehenssion
double_number=[n*2 for n in range(1,5)]
print(double_number)



name ="Rakshit"
letter_list = [letter for  letter in name]
print(letter_list)

names = ["rakshit", "jay","priya","lakshy"]
names[2]= "priyal"
print(names)
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(strings) for strings in list_of_strings]

result =[even for even in numbers if even%2==0] 
print(result)