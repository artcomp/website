import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/avaliar')
def avaliar():
	return render_template("avaliar.html", title='New News Title')


if __name__ == '__main__':
	app.run(debug=True)
