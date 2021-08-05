from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # homepage
def home():
    return render_template("home.html")


@app.route('/contact/')  # homepage
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
