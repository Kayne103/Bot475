from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import request

app = Flask(__name__, static_url_path='/static')
english_bot = ChatBot("Chatterbot",
                      storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                      database="bot475",
                      database_uri="mongodb+srv://admin:bot475@bot475.7nld2.mongodb.net/bot475?"
                                   "retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == '__main__':
    app.run()
