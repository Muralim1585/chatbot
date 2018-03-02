import time

user_template = "User: {0}"
bot_template = "Bot: {0}"

def respond(message):
	bot_message = "I can hear you! You said: " + message
	return bot_message

def send_message(message):
	message = input(user_template.format(message))
	time.sleep(0.5)
	if(message != 'exit'):
		message = respond(message)
		print(bot_template.format(message) + '\n')
		send_message('')
	else:
		message = "Good bye, User!"
		print(bot_template.format(message))
		

send_message('')