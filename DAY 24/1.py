try :
    file = open("File.txt")
    contents = file.read()
    print(contents)
except FileNotFoundError:
    print("file was not exisiting ")
    print("I created one for you")
    file = open("File.txt","w")

file.close()

# using the with keyword

# with open("anotherfile.txt","w")as file:
#     contents = file.read()
#     print(contents)


with open("anotherfile.txt","w")as file:
    contents = file.write("This is the course of python")
    print(contents)
