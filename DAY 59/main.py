from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")  # You can create about.html later

@app.route('/contact')
def contact():
    return render_template("contact.html")  # You can create contact.html later

if __name__ == "__main__":
    app.run(debug=True)
