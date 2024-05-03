from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
