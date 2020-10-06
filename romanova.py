import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = telebot.TeleBot("Aqui va el token de telegram")

def bot_conversacional(message):
	chatbot = ChatBot(
                'fiodorovna',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.BestMatch'
                ],
                database_uri='sqlite:///database.sqlite3'
        )



	trainer = ChatterBotCorpusTrainer(chatbot)

	#Solo se descomenta las siguiente dos lineas de codigo para entrenamiento

	#chatbot= ChatBot("fiodorovna",trainer = "chatterbot.trainers.ChatterBotCorpusTrainer")
	#trainer.train("chatterbot.corpus.spanish","chatterbot.corpus.english","chatterbot.corpus.custom.myown")

	respuesta = chatbot.get_response(message)
	respuesta = str(respuesta)


	mensaje = open("respuesta.txt", "w")
	mensaje.write(respuesta)
	mensaje.close()



@bot.message_handler(commands=['whoami'])
def enviar_mensaje(message):
	bot.reply_to(message, "Hola soy Alejandra Fiódorovna Románova. 'La emperatriz de rusia'")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
	bot_conversacional(message.text)
	respuesta = open("respuesta.txt", "r")
	respuesta = respuesta.read()
	bot.reply_to(message,respuesta)


bot.polling()



