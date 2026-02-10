from flask import Flask, render_template, request, redirect, session
import json
import hashlib
import os

file_path = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(file_path, "templates")
users_file = os.path.join(file_path, "users.json")

app = Flask(__name__, template_folder=template_folder)
app.secret_key = "secret123"

def load_users():
    try:
        with open(users_file, "r") as f:
            users = json.load(f)
    except:
        users = {}
    return users

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_tasks(username):
    users = load_users()
    if username in users:
        return users[username]["tasks"]
    return []

def save_user_tasks(username, tasks):
    users = load_users()
    if username in users:
        users[username]["tasks"] = tasks
        save_users(users)

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        tasks = get_user_tasks(username)
        return render_template("index.html", tasks=tasks, username=username)
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        
        if username in users and users[username]["password"] == hash_password(password):
            session["username"] = username
            return redirect("/")
        else:
            return render_template("login.html", error="Wrong username or password")
    
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()
        
        if username in users:
            return render_template("signup.html", error="Username already exists")
        
        users[username] = {"password": hash_password(password), "tasks": []}
        save_users(users)
        session["username"] = username
        return redirect("/")
    
    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/add", methods=["POST"])
def add():
    if "username" not in session:
        return redirect("/login")
    
    username = session["username"]
    task = request.form.get("task")
    tasks = get_user_tasks(username)
    tasks = tasks + [task]
    save_user_tasks(username, tasks)
    return redirect("/")

@app.route("/delete/<int:num>", methods=["GET"])
def delete(num):
    if "username" not in session:
        return redirect("/login")
    
    username = session["username"]
    tasks = get_user_tasks(username)
    tasks = tasks[:num-1] + tasks[num:]
    save_user_tasks(username, tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
