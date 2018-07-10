
def send_telegram_message(text, chat_id, bot_token):
	import telegram
	bot = telegram.Bot(bot_token)
	bot.send_message(chat_id=chat_id, text=text)

if __name__ == '__main__':
	import sys
	import secrets
	text = "Your process is done"
	if len(sys.argv) == 2:
		text = sys.argv[1]
	try:
		send_telegram_message(text, secrets.tele_chat_id, secrets.tele_token)
	except:
		print("Something went wrong with telegram_bot")
