import time
import re

user_template = "User: {0}"
bot_template = "Bot: {0}"

keywords = {
	"goodbye": [
		"bye",
		"farewell"],
	"greet": [
		"hello",
		"hi",
		"hey"],
	"thankyou": [
		"thank",
		"thx"]
}

responses = {
	"default": "default message",
	"goodbye": "Goodbye for now",
	"greet": "Hello you",
	"thankyou": "You are very welcome"
}

# Creates patterns dictionary
patterns = {}

for intent, keys in keywords.items():
	patterns[intent] = re.compile("|".join(keys))

print(patterns)

# Function to find the intent of a message
def match_intent(message):
	matched_intent = None
	for intent, pattern in patterns.items():
		if pattern.search(message):
			matched_intent = intent
	return matched_intent

def respond(message):
	intent = match_intent(message)
	key = "default"
	if intent in responses:
		key = intent
	return responses[key]

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