# try:
#     with open("a_file.text") as file:
#         file.read()
# except FileNotFoundError:
#     with open("a_file.txt","w")as file:
#             file.write("some  ")

# user_age = int(input("Enter your age"))
# try:
#     if user_age<18:
#          raise ValueError
#     print("You are elligible for the vote")
# except ValueError:
#      print("you are not an adult")
     

# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
    
    
#     try:
#         fruit = fruits[index]
#         # TODO: write code...
#         print(fruit + " pie")
        
#     except IndexError:
#         print("fruit pie")
 

# make_pie(4)





facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

 
def count_likes(posts):
 
    total_likes = 0
    for post in posts:
      try:
        total_likes = total_likes + post['Likes']
      except KeyError:
        pass 
    
    return total_likes
 
 
print(count_likes(facebook_posts))

