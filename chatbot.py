from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("chatbot")

chatbot.set_trainer(ListTrainer)

def train(statement):
	chatbot.train(statement)

def speech(ask):
	return chatbot.get_response(ask).text