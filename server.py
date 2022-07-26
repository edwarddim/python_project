from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"


@app.route('/register', methods=["post"])
def register():
    User.save(request.form)
    return redirect('/dashboard')


@app.route("/login")
def login():
    return "login.html"

