import time
import random
import re

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


rules = {
	"I want (.*)": [
		"What would it mean if you got {0}",
		"Why do you want {0}",
		"Waht's stopping you from getting {0}"],
	"Do you remember (.*)": [
		"Did you think I would forget {0}",
		"Why haven't you been able to forget {0}",
		"What about {0}",
		"Yes... And?"],
	"Do you think (.*)": [
		"If {0}? Absolutely.",
		"No chance"],
	"If (.*)": [
		"Do you really think it's likely that {0}",
		"Do you wish that {0}",
		"What do you think about {0}",
		"Really? If {0}"]
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

def match_rule(rules, message):
	response, phrase = "default", None
	for pattern, responses in rules.items():
		match = re.search(pattern, message)
		if match is not None:
			response = random.choice(responses)
			if '{0}' in response:
				phrase = match.group(1)
	return response, phrase

print(match_rule(rules, "Do you remember your last birthday"))
