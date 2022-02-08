From flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Under Construction"

@app.rout('/login', methods =["POST", "GET"])
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



if __name__ == "__main__":
    app.run()