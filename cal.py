from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("calc.html")

@app.route("/add",methods=["get","post"])
def add():
	a = request.form["param1"]
	b = request.form["param2"]
	operation = request.form["param3"]
	if operation == "1":
		c = int(a)+int(b)
	elif operation == "2":
		c = int(a)-int(b)
	elif operation == "3":
		c = int(a)*int(b)
	else:
		c = int(a)/int(b)
	return str(c)

if __name__ == "__main__":
	app.run(debug=True)
