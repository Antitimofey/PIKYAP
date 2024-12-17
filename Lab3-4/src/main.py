import telebot

bot = telebot.TeleBot('7827687652:AAGyNjGzZlCgW8OUdRSLxvAM5ykkfXmSRKg')

# all text exept commands


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('перейти на сайт ros2')
    btn2 = types.KeyboardButton('удалить фото')
    btn3 = types.KeyboardButton('изменить фото')
    markup.add(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, "Доступные действия:", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'перейти на сайт ros2':
        bot.send_message(message.chat.id, "перехожу на сайт...")
    else:
        bot.send_message(message.chat.id, "это сообщение пока не может быть обработано")


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <u><em>info</em></u>',
                     parse_mode='html')
    print(message)

@bot.message_handler(commands=['get_user_info'])
def main(message):
    bot.reply_to(message, f"your id is {message.from_user.id}")
    print(message)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'my id':
        bot.reply_to(message, f"your id is {message.from_user.id}")
        #process photo


#----------------------maybe lab 5?-----------------
from telebot import types

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('перейти на сайт ros2', url='https://docs.ros.org/en/rolling/Releases/Release-Jazzy-Jalisco.html')
    btn2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('изменить фото', callback_data='change')
    markup.add(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, "photo loaded", reply_markup=markup)

#-------------------??????????????????????-------------------------------
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    print('callback works')
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message.id)
    elif callback.data == 'change':
        bot.edit_message_text('text edited', callback.message.chat.id, callback.message.message.id)





bot.polling(none_stop=True)