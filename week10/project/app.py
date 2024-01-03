import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required
from bs4 import BeautifulSoup
import requests


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

subjects = (
    "Azeri",
    "Biology",
    "Business Accounting",
    "Business Writing",
    "Chemistry",
    "Chinese",
    "Computer Science",
    "English",
    "Geography",
    "German",
    "Health",
    "History",
    "ICT",
    "Math",
    "Physical Education",
    "Physics",
    "Psychology",
    "Public Speaking",
    "Russian",
    "S.St",
    "Spanish"
)

parts = (
    "Noun",
    "Adjective",
    "Verb",
    "Adverb",
    "Conjuction",
    "Abbreviation",
    "Exclamation",
    "Interjection"
)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/homework", methods=["GET", "POST"])
@login_required
def homework():
    if request.method == 'GET':
        homework = db.execute("SELECT * FROM homework WHERE user_id = ? ORDER BY deadline", session["user_id"])
        return render_template("homework.html", homework=homework)


@app.route("/addHomework", methods=["GET", "POST"])
@login_required
def addHomework():
    if request.method == 'POST':
        subject = request.form.get("subject")
        requirements = request.form.get("requirements").capitalize()
        deadline = request.form.get("deadline")
        description = request.form.get("description").capitalize()

        if not subject or not description or not requirements:
            flash("Fill in all the required fields")
            return render_template("/addHomework.html", subjects=subjects)
        elif subject not in subjects:
            flash("Error")
            return render_template("/addHomework.html", subjects=subjects)

        db.execute("INSERT INTO homework (user_id, subject, materials_required, deadline, description) VALUES(?, ?, ?, ?, ?)",
                    session["user_id"], subject, requirements, deadline, description)

        return redirect("/homework")

    else:
        return render_template("/addHomework.html", subjects=subjects)


@app.route("/completed", methods=["GET", "POST"])
@login_required
def completed():

    id = request.form.get("id")
    if not id:
        flash("Error")

    db.execute("DELETE FROM homework WHERE id = ?", id)
    flash("Well done!")

    return redirect("/homework")


@app.route("/vocab", methods=["GET", "POST"])
@login_required
def vocab():
    if request.method == 'GET':
        vocab = db.execute("SELECT * FROM vocab WHERE user_id = ? ORDER BY word", session["user_id"])
        return render_template("vocab.html", vocab=vocab)


@app.route("/addWord", methods=["GET", "POST"])
@login_required
def addWord():
    if request.method == 'POST':
        word = request.form.get("word")
        part = request.form.get("part")
        definition = request.form.get("definition")
        synonym = request.form.get("synonym")
        antonym = request.form.get("antonym")
        sample = request.form.get("sample")

        if not word or not part or not definition:
            flash("Fill in all the required fields")
            return render_template("/addWord.html", parts=parts)

        elif part not in parts:
            flash("Error")
            return render_template("/addWord.html", parts=parts)

        db.execute("INSERT INTO vocab (user_id, word, part, definition, synonym, antonym, sample) VALUES(?, ?, ?, ?, ?, ?, ?)",
                    session["user_id"], word, part, definition, synonym, antonym, sample)

        return redirect("/vocab")

    else:
        return render_template("/addWord.html", parts=parts)



@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():

    id = request.form.get("id")
    if not id:
        flash("Error")

    db.execute("DELETE FROM vocab WHERE id = ?", id)
    return redirect("/vocab")

@app.route("/login", methods=["GET", "POST"])
def login():
     # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return render_template("login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/ ")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        newUsername = request.form.get("username")
        newPassword = request.form.get("password")
        verifyPassword = request.form.get("confirmation")

        # Ensure username was submitted
        if not newUsername:
            flash("must provide username")
            return render_template("register.html")

        # Ensure that the username doesn't exist
        check = db.execute("SELECT username FROM users")
        for i in check:
            if i["username"] == newUsername:
                flash("username exists")
                return render_template("register.html")

        # Ensure password was submitted
        if not newPassword:
            flash("must provide password")
            return render_template("register.html")

        # Ensure password was submitted
        elif not verifyPassword or not newPassword == verifyPassword:
            flash("password doesn't match")
            return render_template("register.html")


        # Hash the Password
        hashedPassword = generate_password_hash(newPassword, method='pbkdf2:sha256', salt_length=7)
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", newUsername, hashedPassword)
        id = db.execute("SELECT id FROM users WHERE username = ?", newUsername)

        # Remember which user has logged in
        session["user_id"] = id[0]['id']

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/addWordDict", methods=["GET", "POST"])
@login_required
def addWordDict():
    if request.method == 'POST':
        word = request.form.get("word").lower()

        if not word:
            flash("Fill in all the required fields")
            return render_template("addWordDict.html")


        web2 = requests.get("https://www.britannica.com/dictionary/" + word)
        data2 = web2.content
        soup2 = BeautifulSoup(data2, features="html.parser")

        web3 = requests.get("https://sentence.yourdictionary.com/" + word)
        data3 = web3.content
        soup3 = BeautifulSoup(data3, features="html.parser")

        web4 = requests.get("https://www.wordhippo.com/what-is/the-opposite-of/" + word + ".html")
        data4 = web4.content
        soup4 = BeautifulSoup(data4, features="html.parser")

        web5 =  requests.get("https://www.wordhippo.com/what-is/another-word-for/" + word + ".html")
        data5 = web5.content
        soup5 = BeautifulSoup(data5, features="html.parser")

        web6 =  requests.get("https://www.wordhippo.com/what-is/the-meaning-of-the-word/" + word + ".html")
        data6 = web6.content
        soup6 = BeautifulSoup(data6, features="html.parser")

        d = soup2.find_all("span", "def_text")
        part = soup6.find_all("div", "defv2wordtype")
        synonym = soup5.find_all("div", "wb")
        antonym = soup4.find_all("div", "wb")
        sample = soup3.find_all("p", "sentence-item__text")



        a = 0
        for i in synonym:
            if a == 0:
                synonym2 = i
            elif a == 3:
                break
            else:
                synonym2.append(", ")
                synonym2.append(i)
            a += 1

        a = 0
        for i in antonym:
            if a == 0:
                antonym2 = i
            elif a == 3:
                break
            else:
                antonym2.append(", ")
                antonym2.append(i)
            a += 1

        a = 0
        part2 = []
        for i in part:
            if a == 0:
                part2.append(i)
                # part2 = i.text
            else:
                if i not in part2:
                    part2.append(i)
            a += 1

        a = 0
        part3 = []
        for i in part2:
            if a == 0:
                part3.append(i.text)
                # part2 = i.text
            else:
                part3.append(i.text)
            a += 1

        string = ', '.join(map(str,part3))





        try:
            id = db.execute("INSERT INTO vocab (user_id, word, part, definition, sample, synonym, antonym) VALUES(?,?, ?, ?, ?, ?, ?)",
            session["user_id"], word, string, d[0].text, sample[0].text, synonym2.text, antonym2.text)
        except:
            flash("Word could not be found")
            return redirect("/vocab")

        if len(d) > 1:
            db.execute("UPDATE vocab SET d1 = ? WHERE id = ?", d[1].text, id)
        if len(d) > 2:
            db.execute("UPDATE vocab SET d2 = ? WHERE id = ?", d[2].text, id)
        if len(d) > 3:
            db.execute("UPDATE vocab SET d3 = ? WHERE id = ?", d[3].text, id)
        if len(d) > 4:
            db.execute("UPDATE vocab SET d4 = ? WHERE id = ?", d[4].text, id)
        if len(d) > 5:
            db.execute("UPDATE vocab SET d5 = ? WHERE id = ?", d[5].text, id)
        if len(d) > 6:
            db.execute("UPDATE vocab SET d6 = ? WHERE id = ?", d[6].text, id)
        if len(d) > 7:
            db.execute("UPDATE vocab SET d7 = ? WHERE id = ?", d[7].text, id)
        if len(d) > 8:
            db.execute("UPDATE vocab SET d8 = ? WHERE id = ?", d[8].text, id)
        if len(d) > 9:
            db.execute("UPDATE vocab SET d9 = ? WHERE id = ?", d[9].text, id)
        if len(d) > 10:
            db.execute("UPDATE vocab SET d10 = ? WHERE id = ?", d[10].text, id)
        if len(d) > 11:
            db.execute("UPDATE vocab SET d11 = ? WHERE id = ?", d[11].text, id)

        return redirect("/vocab")

    else:
        return render_template("/addWordDict.html", parts=parts)



@app.route("/resetPassword", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == 'POST':
        oldPassword = request.form.get("oldPassword")
        newPassword = request.form.get("newPassword")
        confirmation = request.form.get("confirmation")

        # Ensure old password was submitted
        if not oldPassword:
            flash("must provide old password")
            return render_template("resetPassword.html")

        # Ensure new password was submitted
        if not newPassword:
            flash("must provide new password")
            return render_template("resetPassword.html")

        # Ensure password was submitted
        elif not confirmation or not newPassword == confirmation:
            flash("confirmation password doesn't match")
            return render_template("resetPassword.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], oldPassword):
            flash("wrong password")
            return render_template("resetPassword.html")

        # Ensure that new password isn't the same as the old password
        if oldPassword == newPassword:
            flash("your new password can't be your old password")
            return render_template("resetPassword.html")

        # Hash the Password
        hashedPassword = generate_password_hash(newPassword, method='pbkdf2:sha256', salt_length=3)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hashedPassword, session["user_id"])

        return redirect("/")

    else:
        return render_template("resetPassword.html")