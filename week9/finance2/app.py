import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd


# export API_KEY=pk_f7761128e52448749eb13f0dc7470e9c

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    stocks = db.execute("SELECT symbol, shares FROM stocks WHERE id = ?", user_id)
    for stock in stocks:
        price = lookup(stock["symbol"])
        total_price = stock["shares"] * price["price"]
        db.execute("UPDATE stocks SET price = ?, total_price = ? WHERE id = ? AND symbol = ?", price["price"], total_price, session["user_id"], stock["symbol"])
    stocks = db.execute("SELECT * FROM stocks WHERE id = ?", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash[0]["cash"]
    total = cash
    for stock in stocks:
        total = total + stock["total_price"]

    return render_template("index.html", stocks = stocks, cash = cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide stock's symbol")
        elif not shares:
            return apology("must provide number of shares")

        response = lookup(symbol)
        if not response:
            return apology("must provide valid symbol")

        price = response["price"]
        name = response["name"]
        cash1 = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = cash1[0]["cash"]
        total_price = int(shares) * price
        if cash < total_price:
            return apology("can't afford the number of shares")

        cash = cash - total_price

        now = datetime.datetime.now()

        type = "Bought"

        stock_symbol = ("SELECT name, shares FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol)

        db.execute("INSERT INTO history (id, symbol, shares, price, transaction_type, time) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], symbol, shares, price, type, now)
        # If the user has never bought from that company a stock
        if not stock_symbol[0]["name"]:
            db.execute("INSERT INTO stocks (id, symbol, name, shares, price, total_price) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], symbol, name, shares, price, total_price)
         # If the user has already bought from that company a stock
        else:
            shares = stock_symbol[0]["shares"] + shares
            total_price = shares * price
            db.execute("UPDATE stocks SET shares = ?, total_price = ? WHERE id = ? and symbol = ?", shares, total_price, session["user_id"], symbol)

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide stock's symbol")
        response = lookup(symbol)
        if not response:
            return apology("must provide valid stock's symbol")

        return render_template("quoted.html", stock = response)

     # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


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
            return apology("must provide username")

        # Ensure that the username doesn't exist
        # check = db.execute("SELECT username FROM users")
        # for i in check:
        #     if i["username"] == newUsername:
        #         return apology("username exists")

        # Ensure password was submitted
        if not newPassword:
            return apology("must provide password")

        # Ensure password was submitted
        elif not verifyPassword or not newPassword == verifyPassword:
            return apology("password doesn't match")

        # Hash the Password
        hashedPassword = generate_password_hash(newPassword, method='pbkdf2:sha256', salt_length=3)
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", newUsername, hashedPassword)

        # Remember which user has logged in
        session["user_id"] = id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # Obtain the stock's symbol ad the amount of shares that will be sold
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # From SQL obtain the amount of shares of a stock that the user owns and the price of it
        sell_stock = db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol)
        user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        price = lookup(symbol)
        price = price["price"]

        # If the user didn't provide any symbols
        if not symbol:
             return apology("must provide stock's symbol")

        # If the user didn't provide the amount of shares
        if not shares:
            return apology("must provide number of shares")

        # If the user inputs a negative number of shares or more than they own
        if int(shares) < 0 or int(shares) > sell_stock[0]["shares"]:
            return apology("must provide valid number of shares")

        # Add the profit of selling the share(s)
        user[0]["cash"] += price * int(shares)

        # Calculate the amount of the shares of a company that the user owns currently
        current_shares = sell_stock[0]["shares"] - int(shares)

        # Calculate the current total price of the stock
        current_total_price = current_shares * price

        now = datetime.datetime.now()
        type = "Sold"
        db.execute("INSERT INTO history (id, symbol, shares, price, transaction_type, time) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], symbol, shares, price, type, now)

        # Update the money that the user has in their bank account
        db.execute("UPDATE users SET cash = ? WHERE id = ?", user[0]["cash"] , session["user_id"])

        # If the user sells all of the shares that they own
        if int(shares) == sell_stock[0]["shares"]:
            db.execute("DELETE FROM stocks WHERE id = ? AND symbol = ?", session["user_id"], symbol)
        else:
            db.execute("UPDATE stocks SET shares = ?, total_price = ? WHERE id = ? AND symbol = ?", current_shares, current_total_price, session["user_id"], symbol)

        return redirect("/")

    else:
        symbol = db.execute("SELECT symbol FROM stocks WHERE id = ?", session["user_id"])
        return render_template("sell.html", stocks=symbol)