from flask import Flask, render_template
import random
import requests
from datetime import datetime

app = Flask(__name__)

def random_num():
    return random.randint(0, 5)

def current_year():
    return datetime.now().year

@app.route("/")
def home():
    number = random_num()
    year = current_year()
    return render_template("index.html", num=number, year=year, my_name="Rakshit Bagait")

@app.route("/guess/<name>")
def guess(name):
    try:
        gender_url = f"https://api.genderize.io?name={name}"
        gender_response = requests.get(gender_url)
        gender_response.raise_for_status()
        gender_data = gender_response.json()
        gender = gender_data.get("gender", "Unknown")

        age_url = f"https://api.agify.io?name={name}"
        age_response = requests.get(age_url)
        age_response.raise_for_status()
        age_data = age_response.json()
        age = age_data.get("age", "Unknown")
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        gender = "Error"
        age = "Error"
        
    return render_template("guess.html", person_name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/5abcca6f4339b4955965"
    try:
        response = requests.get(blog_url)
        response.raise_for_status()
        all_posts = response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch blog data: {e}")
        all_posts = []
    
    return render_template("blog.html", posts=all_posts, title="My Blog")

if __name__ == "__main__":
    app.run(debug=True)
