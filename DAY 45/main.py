from bs4 import BeautifulSoup
with open("D:/100 Days Of Python/DAY 45/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,'html.parser')
print(soup.title.string)

print(soup.prettify())

print(soup.p)

all_para = soup.find_all(name='p')
print(all_para)

for tag in all_para:
    print(tag.getText())

heading = soup.find(name="h1",id="name")
print(heading)

section_heading = soup.find(name="h3",class_ = "heading")
print(section_heading.string)