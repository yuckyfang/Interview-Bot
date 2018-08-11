from flask import Flask, render_template, request
from P import QuestionList, goodResponseList
import random
from leetcode import *

app = Flask(__name__)

messages_log = []
chat_log = []
d_log = []

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == 'GET':
		del chat_log[:]
		del messages_log[:]
		return render_template('index.html')
	elif request.method == 'POST':
		if len(messages_log) > 2:
			tech_question = get_random_question()
			description = tech_question.get_description()
			solution = tech_question.get_solution()

			if len(d_log) > 0:
				print('HELLO')
				chat_log.append(solution)
				return render_template('index.html', messages=chat_log)			
			chat_log.append('Please answer this coding question: ')
			chat_log.append(description)
			d_log.append(description)
			return render_template('index.html', messages=chat_log)
		else:
			message = request.form['message']
			question = QuestionList[len(messages_log) - 1]
			response = goodResponseList[len(messages_log) - 2]
			chat_log.append(message)
			messages_log.append(message)
			if len(chat_log) > 2:
				chat_log.append(response)
			chat_log.append(question)
			return render_template('index.html', messages=chat_log)
	



if __name__ == '__main__':
	app.run(debug = True)