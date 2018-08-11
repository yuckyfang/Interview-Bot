from flask import Flask, render_template, request
from P import QuestionList, goodResponseList
import random
from leetcode import *
import os
import sys
import pyttsx3
from speech2text import recognize_speech_from_mic



app = Flask(__name__)

engine = pyttsx3.init()
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
				chat_log.append("Thanks for your response. Here's the solution:")
				chat_log.append(solution)
				return render_template('index.html', messages=chat_log)			
			chat_log.append('Please answer this coding question: ')
			chat_log.append(description)
			d_log.append(description)
			return render_template('index.html', messages=chat_log)
		else:
			#message = request.form['message']
			message = recognize_speech_from_mic()
			question = QuestionList[len(messages_log) - 1]
			response = goodResponseList[len(messages_log) - 2]
			chat_log.append(message)
			messages_log.append(message)
			if len(chat_log) > 2:
				chat_log.append(response)
				engine.say(response)
				engine.runAndWait()
			chat_log.append(question)
			engine.say(question)
			engine.runAndWait()
			return render_template('index.html', messages=chat_log)
	



if __name__ == '__main__':
	app.run(debug = True)