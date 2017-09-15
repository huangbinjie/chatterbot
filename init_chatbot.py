"""
如果没有 db.sqlite3 这个文件就需要跑下这个脚本初始化之
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("chatbot")

# 设置训练方法：词汇表。手工训练是 ListTrainer
chatbot.set_trainer(ChatterBotCorpusTrainer)

# https://github.com/gunthercox/chatterbot-corpus
chatbot.train("chatterbot.corpus.chinese")
