import time

user_template = "User: {0}"
bot_template = "Bot: {0}"

name = "Gigi"
weather = "cloudy"

responses = {
	"What's your name?": "My name is {0}".format(name),
	"What's today's weather?": "The weather is {0}".format(weather),
	"default": "Massa"
}

def respond(message):
	if message in responses:
		bot_message = responses[message]
	else:
		bot_message = responses["default"]
	return bot_message

def send_message(message):
	message = input(user_template.format(message))
	time.sleep(0.5)
	if(message != "exit"):
		message = respond(message)
		print(bot_template.format(message) + "\n")
		send_message('')
	else:
		message = "Good bye, User!"
		print(bot_template.format(message))

send_message('')