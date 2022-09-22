import telebot
import psycopg2
import datetime


token = "5016970397:AAGNgxWFTsbH8glxfqHFABWe-tYSWZFJnpQ"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "Не хочу")
    keyboard.row("Да", "Нет")
    bot.send_message(message.chat.id, "Привет! хочешь узнать новую информацию о МТУСИ?", reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Я умею...")


@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == "хочу" or message.text.lower() == "да":
        bot.send_message(message.chat.id, "Тогда тебе сюда - mtuci.ru")
    elif message.text.lower() == "не хочу" or message.text.lower() == "нет":
        bot.send_message(message.chat.id, "Ладно... Понятно...Пока...")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял...")


bot.infinity_polling()
