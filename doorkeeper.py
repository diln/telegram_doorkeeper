import telebot
import os

# Настройки бота
bot_token = os.environ.get('bot_token')
bot = telebot.TeleBot(bot_token)


@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    username = message.new_chat_members[0].first_name
    bot.reply_to(message, text=f'{username}, добро пожаловать!\nБудет здорово, если вы представитесь и расскажете '
                               f'в каком IT-направлении сильны или хотели бы развиваться \U0001F609')


if __name__ == '__main__':
    bot.polling(none_stop=True)
