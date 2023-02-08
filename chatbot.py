#  train using the your own text file.

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Test')

for _file in os.listdir('files'):
    chats = open('files/' + _file, 'r').readlines()

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ',  response)


#  train using the default

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# bot = ChatBot('My ChatBot',
#         storage_adapter='chatterbot.storage.SQLStorageAdapter',
#         database_uri='sqlite:///chatbot.sqlite3'
#         )

# trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.english")

# while True:
#     user_input = input("User: ")
#     bot_response = bot.get_response(user_input)
#     print("Bot: ", bot_response)
