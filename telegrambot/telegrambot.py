import telebot
import random

bot = telebot.TeleBot('338955990:AAF16KS0tE5BJtiSZJb56yO5we7pxECWo7c')

@bot.message_handler(commands = ['start'])
def first_message(message):
     bot.send_message(message.chat.id, "I'm a bot, there is no point to talk to me.")
     bot.send_message(message.chat.id,"But if you haven't got friends we can chat a bit.")
     bot.send_message(message.chat.id, "There are my options: /help, /prediction, /pic")

@bot.message_handler(commands = ['prediction'])
def prediction(message):
     prediction_list = random.choice (["You'll die alone.","Nothing will be good","No future for you",
                                       "Life is pain","You can't do it"])
     bot.send_message(message.chat.id, prediction_list)
     bot.send_message(message.chat.id,"Another one /prediction")

@bot.message_handler(commands = ['help'])
def send_help(message):
     bot.send_message(message.chat.id, "Nobody can help you")

@bot.message_handler(commands = ['pic'])
def pic(message):
     bot.send_message(message.chat.id, "Enjoy")
     photorandom = random.choice (['photo/photo0.jpg',
                                   'photo/photo1.jpg',
                                   'photo/photo2.jpg',
                                   'photo/photo3.jpg',
                                   'photo/photo4.jpg',
                                   'photo/photo5.jpg'])
     photo = open(photorandom, 'rb')
     bot.send_photo(message.chat.id, photo)
     bot.send_message(message.chat.id, "More /pic")


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
     #bot.send_message(message.chat.id, "I tired of you")
     bot.send_message(message.chat.id, message.text)


bot.polling()
