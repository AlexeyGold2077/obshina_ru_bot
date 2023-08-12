from private import TOKEN
import telebot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command_responce(message):
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name} {message.from_user.last_name} приветствуем тебя в боте русской общины!\nНапиши /help для отображения доступных команд или нажми на кнопку команды ниже.')

@bot.message_handler(commands=['help'])
def help_command_responce(message):
    bot.send_message(message.chat.id, 'Список доступных комманд:\n/help - список доступных комманд\n/channel - получить ссылку на наш официальный телеграм канал')

@bot.message_handler(commands=['channel'])
def channel_command_responce(message):
    bot.send_message(message.chat.id, 'Наш официальный канал в телеграм - @obshina_ru')

bot.polling(none_stop=True)