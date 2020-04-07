from telebot import *
import encryptionDanqi as enc
from time import *
import config
bot=TeleBot(config.token)
type=[" "]*1000000000
get_start0=[0]*1000000000
sleep(40)
print("type-ok")

types_markup=types.ReplyKeyboardMarkup(one_time_keyboard=True)
types_markup.add("1","2","3")
hideBoard = types.ReplyKeyboardRemove()
@bot.message_handler(commands=["start"])
def get_start(message):
    global get_start0
    if get_start0[message.chat.id]==0:
        get_start0[message.chat.id]=1
        bot.reply_to(message,"Привіт "+message.from_user.first_name+", давай почнемо.")
        sleep(1)
        bot.send_message(message.chat.id, "Напиши /help для допомоги.")
        print(message.chat.id)


@bot.message_handler(commands=["help"])
def get_help(message):
    bot.reply_to(message,""" Пиши /encrypt для шифрування
Пиши /decrypt для дешифрування
Удачі тобі)
""")

@bot.message_handler(commands=["help_type"])
def get_help_wiht_types(message):
    bot.reply_to(message,"Значить так...")
    sleep(1)
    bot.send_message(message.chat.id,"Тип №1 використовується лише для чисел")
    sleep(2)
    bot.send_message(message.chat.id,"Тип №2 використовується для любих символів окрім емодзі")
    sleep(3)
    bot.send_message(message.chat.id,"Тип №3 схожий з типом №2, проте в нього посилений захист")


@bot.message_handler(commands=["encrypt"])
def get_encrypt00(message):
    msg=bot.send_message(message.chat.id,"""Впиши тип шифрування.
Для допомоги пиши /help_type .
""",reply_markup=types_markup)
    bot.register_next_step_handler(msg, encrypt0)
def encrypt0(message):
    global type
    type[message.chat.id]=str(message.text)
    msg=bot.send_message(message.chat.id,"Напиши текст для шифрування.")
    bot.register_next_step_handler(msg, encrypt)
def encrypt(message):
    global type
    bot.send_message(message.chat.id,"Твій шифр:")
    bot.send_message(message.chat.id,enc.convert(type=int(type[message.chat.id]),text=message.text),reply_markup=hideBoard)


@bot.message_handler(commands=["decrypt"])
def get_decrypt00(message):
     msg=bot.send_message(message.chat.id,"""Впиши тип дешифрування.
Для допомоги пиши /help_type .
""",reply_markup=types_markup)
     bot.register_next_step_handler(msg, decrypt0)
def decrypt0(message):
    global type
    type[message.chat.id]=str(message.text)
    msg=bot.send_message(message.chat.id,"Напиши шифр для дешифрування.")
    bot.register_next_step_handler(msg, decrypt)
def decrypt(message):
    global type
    bot.send_message(message.chat.id,"Твій текст:")
    bot.send_message(message.chat.id,enc.unconvert(type=int(type[message.chat.id]),text=message.text),reply_markup=hideBoard)

@bot.message_handler(content_types=["text"])
def text(message):
    bot.reply_to(message,"Емм...")
    sleep(1)
    bot.reply_to(message,"Я тебе трішечки не розумію(")
    sleep(1)
    bot.reply_to(message,"Напиши /help для допомоги")
    sleep(1)

bot.polling(none_stop=True)
