import requests
from bs4 import BeautifulSoup

URL ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response= requests.get(URL)
website_html = response.text
soup =BeautifulSoup(website_html,"html.parser")

# print(soup.prettify())

movies = soup.find_all(name='h3',class_="title")
hundered_movies = [movie.getText() for movie in movies]
rev_list = hundered_movies[::-1]
print(rev_list)

with open("movies.txt","w",encoding="utf-8") as file :
    for item in rev_list:
        file.write(f"{item}\n")
