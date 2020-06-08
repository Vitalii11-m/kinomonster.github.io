from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/films")
def films():
	return render_template("films.html")

@app.route("/films/interstellar")
def interstellar():
	return render_template("interstellar.html")



@app.route("/sirials")
def sirials():
	return render_template("sirials.html")

@app.route("/rating")
def rating():
	return render_template("rayting.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
	app.run(debug = True)