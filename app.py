from flask import Flask, render_template, request, redirect, url_for, session
from diet import calculate_calories, generate_diet
from users import users

app = Flask(__name__)
app.secret_key = "diet_secret_key"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        print("Entered:", username, password)
        print("Stored:", users)

        if users.get(username) == password:
            session["user"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        age = int(request.form["age"])
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        activity = request.form["activity"]
        health = request.form["health"]   # ✅ ONLY health now

        calories = calculate_calories(age, gender, weight, height, activity)
        print("Calories:", calories) 
        diet, advice = generate_diet(calories, health)

        return render_template(
            "result.html",
            calories=calories,
            diet=diet,
            advice=advice
        )

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
