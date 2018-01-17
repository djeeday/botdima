# -*- coding: utf-8 -*-
import telebot,time,re,math

bot = telebot.TeleBot('544871064:AAGzuIJeOPifv4aTPbVqb-wK2O1wXuAgIvI')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    quest=re.search('(\?)', message.text)
    if quest is not None:
        if re.search('(\s\?)', message.text) is not None:
            time.sleep(4)
            bot.send_message(message.chat.id, 'Так'.decode('utf-8'))
            return 1
        else:
            time.sleep(4)
            bot.send_message(message.chat.id, 'Ні'.decode('utf-8'))
            return 1
    x=re.search('(\d+,\d\d\d\d)', message.text)
    time.sleep(8)
    if x is None:
        bot.send_message(message.chat.id, '?')
        return 1
    else:
          m=float(re.sub(',','.',x.group()))
          bot.send_message(message.chat.id, str(int(math.ceil(m *13500/ 100.0)) * 100))
          return 1
    

if __name__ == '__main__':
     bot.polling(none_stop=True)
