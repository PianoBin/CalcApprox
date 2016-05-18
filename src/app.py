from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
	return render_template("index.html")

if __name__ == '__main__':
	app.run()


