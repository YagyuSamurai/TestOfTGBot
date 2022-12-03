import sqlite3
import telebot

bot = telebot.TeleBot("5652554113:AAEsnVG8uCx4NezsRAmep9mubYR2-nS8U6g")

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()



def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute("CREATE TABLE IF NOT EXISTS `database` (`id` INTEGER, `user_id` INTEGER, 'user_name' TEXT, 'user_surname' TEXT, 'username' STRING)")
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()
	




@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Добро пожаловать! Для дальнейшей работы напишите "Привет".')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет! Идёт идентификация вашей личности!')
		print('Привет! Идёт идентификация вашей личности!')


		us_id = message.from_user.id
		us_name = message.from_user.first_name
		us_sname = message.from_user.last_name
		username = message.from_user.username
		cursor.execute(f"SELECT* FROM test where (user_id={us_id}")
		base = cursor.fetchone()
		if base is None:
			db_table_val(user_id = us_id, user_name = us_name, user_surname = us_sname, username = username)
			bot.send_message(message.chat.id, 'Вы успешно были зарегистрированы')
			print('Вы успешно были зарегистрированы')
	
		else:
			bot.send_message(message.chat.id, f'Ваш ID:  {us_id}\nВаше сообщение: {message.text}\nВы успешно авторизовались')
			print(f'Ваш ID:  {us_id}\nВаше сообщение: {message.text}\nВы успешно авторизовались')

	
 
bot.polling(none_stop=True)
