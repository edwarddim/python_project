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

@app.route("/create_recipe")
def create():
    return "create.html"

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route("/update")
def update():
    return "edit.html"

