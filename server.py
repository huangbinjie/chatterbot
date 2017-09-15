from flask import Flask, render_template
from chatbot import speech, train

app = Flask("chatbot_server")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ask/<question>")
def talk(question=None):
	return speech(question)

@app.route("/teach/<q>/<a>")
def teach(q=None,a=None):
	train([q,a])
	return "我已经学会了"
