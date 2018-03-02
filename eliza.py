import time
import random

user_template = "User: {0}"
bot_template = "Bot: {0}"

responses = {
	"question": [
		"I don't know",
		"You tell me"],
	"statement": [
		"Tell me more",
		"Why do you think that?",
		"How long have you felt this way?",
		"I find that extremely interesting",
		"Can you back that up?",
		"Oh, wow"]
}

def respond(message):
	if message.endswith("?"):
		bot_message = random.choice(responses["question"])
	else:
		bot_message = random.choice(responses["statement"])
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
