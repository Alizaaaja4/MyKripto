from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/register")
def register():
	return render_template("createAccount.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5555, debug=True)