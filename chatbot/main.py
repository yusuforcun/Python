from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train("chatterbot.corpus.english")
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)