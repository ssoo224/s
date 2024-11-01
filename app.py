from flask import Flask, render_template, request
import telebot


app = Flask(__name__)

bot = telebot.TeleBot("7533541751:AAHS7A80PdLVOIypjBqw5wYw0z68sUVi7EE")
bot.remove_webhook()


#-----------------------
@app.route('/bot_webhook', methods=['POST'])
def bot_webhook():
  bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
  return 'OK'
@app.route('/set_app', methods=['GET'])
def set_app():
  bot.remove_webhook()
  bot.set_webhook("https://" + request.host + "/bot_webhook")
  return 'Done'
# ----------------------


# https://link.vercel.app/set_app



@bot.message_handler()
def Myfunc(message):
  bot.send_message(message.chat.id, "Hi, What's happend?")




if __name__ == '__main__':
    app.run(debug=True)
