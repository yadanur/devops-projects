from flask import Flask, render_template

app = Flask(__name__)

@app.route("/test")
def head():
  return render_template("index.html", number1=3, number2=45)

@app.route("/body")
def body_page():
  return render_template("body.html")

@app.route("/")
def home():
  return ("this is home page")

if __name__ == "__main__":
  app.run(debug=True)
