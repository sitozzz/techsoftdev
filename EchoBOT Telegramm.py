import telebot
token = "267951772:AAGMkbnYoaibtD9jjNVnn66kESlQpoLSJEs"

bot =  telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])

def start(message):
        sent = bot.send_message(message.chat.id,"Hi everyone there!!!")
        bot.register_next_step_handler(sent,echo)

@bot.message_handler(commands = ['help'])
def help(message):
        bot.send_message(message.chat.id,"It is echo bot, he can't do anything")
       # bot.register_next_step_handler(sent,echo)
def echo(message):
        sent = bot.send_message(message.chat.id, message.text)
        bot.register_next_step_handler(sent,echo)

bot.polling()
