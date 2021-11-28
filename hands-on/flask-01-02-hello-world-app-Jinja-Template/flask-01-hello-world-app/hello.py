from flask import Flask

app= Flask(__name__)

@app.route("/")
def head():
  return "Hello from the other side!"

@app.route("/login")
def login():
  return "This is the login page"

@app.route("/login/error")
def login_error():
  return "Wrong password"

@app.route("/login/<string:userName>")
def loginName(userName):
  return f"Welcome back {userName}"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)

#  app.run(debug=True)
