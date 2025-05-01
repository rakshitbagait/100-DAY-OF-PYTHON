# TODO : Create a letter using starting_lettle.docx
# for each name in inviete_name.txt
# replace the [name] placeholder with the actual name/
# Save the letters in the folder "Ready to send"\

invitation_names =[]
people_count = int(input("Enter the number of people you want to invite"))
for people in range(people_count) :
    names =input("Enter the name of person").capitalize()
    invitation_names.append(names)

with open("invited_names.txt","w")as names_file:
    for invited_names in invitation_names:
            names_file.write(str(invited_names+"\n"))
    names_file.close()
    