from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def iabout():
	return render_template('about.html')


if __name__ == '__main__' :
	app.run(host='127.0.0.1',port=5000,debug=True)