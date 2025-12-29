from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_db_connection():
    return sqlite3.connect("career.db", timeout=10)

@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    if "user" not in session:
        return redirect("/login")
    # rest of your existing logic

    name = request.form.get("name")
    skills = request.form.getlist("skills")

    career = "Frontend Developer"
    required_skills = ["HTML", "CSS", "JavaScript"]
    roadmap = [] 

    if skills == ["HTML"]:
        roadmap = [
            "Learn basic HTML tags",
            "Practice forms and tables",
            "Build static web pages"
        ]

    elif set(skills) == set(["HTML", "CSS"]):
        roadmap = [
            "Learn CSS layouts (Flexbox, Grid)",
            "Make responsive designs",
            "Build styled websites"
        ]

    elif set(skills) == set(["HTML", "CSS", "JavaScript"]):
        roadmap = [
            "Master JavaScript fundamentals",
            "Learn DOM manipulation",
            "Build interactive web apps",
            "Learn React basics"
        ]

    else:
        career = "General IT Career"
        required_skills = ["Programming Basics"]
        roadmap = [
            "Learn basic programming",
            "Choose a specialization",
            "Build beginner projects"
        ]

    skill_gap = list(set(required_skills) - set(skills))

    # SAVE TO DATABASE
    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, skills, career, skill_gap) VALUES (?, ?, ?, ?)",
        (
            name,
            ", ".join(skills),
            career,
            ", ".join(skill_gap)
        )
    )

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        name=name,
        career=career,
        skills=skills,
        skill_gap=skill_gap,
        roadmap=roadmap
    )
@app.route("/users")
def users():
    if "user" not in session:
        return redirect("/login")

    conn = get_db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT id, name, skills, career, skill_gap FROM users")
    data = cursor.fetchall()
    conn.close()

    return render_template("users.html", users=data)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO auth_users (username, password) VALUES (?, ?)",
                (username, password)
            )

            conn.commit()
            conn.close()

            return redirect("/login")

        except sqlite3.IntegrityError:
            message = "Username already exists. Please choose another."

    return render_template("signup.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM auth_users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid username or password"

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
