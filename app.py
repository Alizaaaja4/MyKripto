from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/service")
def service():
	return render_template("service.html")

@app.route("/register")
def register():
	return render_template("createAccount.html")

@app.route("/admin/login")
def adminLogin():
	return render_template("/admin/login.html")

@app.route("/admin/home")
def adminHome():
	return render_template("/admin/home.html")

@app.route("/admin/users")
def adminUsers():
	return render_template("/admin/users.html")

@app.route("/admin/feedback")
def adminFeedback():
	return render_template("/admin/feedback.html")

@app.route("/users/home")
def usersHome():
	return render_template("/users/home.html")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555, debug=True)