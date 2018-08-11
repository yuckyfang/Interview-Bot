from flask import Flask, render_template, request

app = Flask(__name__)

chat_log = []

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == 'POST':
		message = request.form['message']
		chat_log.append(message)

		return render_template('index.html', messages=chat_log)
	elif request.method == 'GET':
		del chat_log[:]
		return render_template('index.html')
if __name__ == '__main__':
	app.run(debug = True)