from flask import Blueprint, render_template, request, redirect, url_for, session
from app.churn_model import predict_churn

main = Blueprint("main", __name__)

# Home Page
@main.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("index.html")


# Login Page
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin":
            session["user"] = username
            return redirect(url_for("main.home"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# Prediction Route
@main.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("main.login"))

    input_data = request.form.to_dict()
    prediction = predict_churn(input_data)

    return render_template("index.html", prediction_result=prediction)


# Logout
@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))