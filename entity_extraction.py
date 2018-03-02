import time
import re

user_template = "User: {0}"
bot_template = "Bot: {0}"

def find_name(message):
	name = None
	name_keyword = re.compile("name|call")
	name_pattern = re.compile("[A-Z]{1}[a-z]*")
	if name_keyword.search(message):
		name_words = name_pattern.findall(message)
		if len(name_words) > 0:
			name = " ".join(name_words)
	return name

def respond(message):
	name = find_name(message)
	if name is None:
		return "Hi, there!"
	else:
		return "Hello, {0}!".format(name)

def send_message(message):
	message = input(user_template.format(message))
	time.sleep(0.5)
	if message != "exit":
		response = respond(message)
		print(bot_template.format(response) + "\n")
		send_message('')
	else:
		response = "Good bye, User!"
		print(bot_template.format(response))

send_message('')