from flask import Flask
import random 
app = Flask(__name__)

app.route('/')

num = random.randint(1,11)
print(num)

if __name__ == "__main__":
    app.run()