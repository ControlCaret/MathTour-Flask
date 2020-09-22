from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/oxexample')
def oxexample():
	return render_template(
		'ox.html',
		displayTitle = "OX Quiz Example Template",
		displayText = "displayText example",
		displayProblem = "displayProblem example",
		quizNumber = 0
	)

@app.route('/check', methods=['POST'])
def quizCheck():
	answer = request.form['ox']
	quizNumber = request.form['quizNumber']
	return answer + ' ' + quizNumber


if __name__ == '__main__':
	app.debug = True
	app.run()
