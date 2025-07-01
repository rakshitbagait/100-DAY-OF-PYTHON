from flask import Flask, render_template, request
import requests, smtplib
app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
my_email ="rbagait2018@gmail.com"
password ="your password"
@app.route("/")

def homepage():
    return render_template("index.html")
@app.route("/login",methods = ["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return render_template("login.html",name = username,password= password)

@app.route("/contact", methods=["GET", "POST"])
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]

        # Format email content from user
        email_body = f"""
You received a new message from your website contact form:

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,  # You receive the email
                    msg=f"Subject: New Contact Message from {name}\n\n{email_body}"
                )
            return "<h1>Successfully sent your message</h1>"
        except Exception as e:
            return f"<h1>Failed to send message. Error: {e}</h1>"

    return render_template("contact.html")



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
