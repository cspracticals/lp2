import random

# A. Asking for the user's name
print("BOT: What is your name?")
user_name = input("You: ")

# B. Predefined responses
name = "Bot Number 286"
monsoon = "rainy"
mood = "Smiley"

resp = {
    "what's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "My name is the {0}".format(name)
    ],
    "what's today's weather?": [
        "The weather is {0}".format(monsoon),
        "It's {0} today".format(monsoon)
    ],
    "how are you?": [
        "I am feeling {0}".format(mood),
        "{0}! How about you?".format(mood),
        "I am {0}! How about yourself?".format(mood)
    ],
    "": [
        "Hey! Are you there?",
        "What do you mean by this?"
    ],
    "default": [
        "I didn't understand that.",
        "Can you say that again?",
        "This is a default message."
    ]
}

# C. Function to choose a response randomly
def res(message):
    if message in resp:
        bot286_message = random.choice(resp[message])
    else:
        bot286_message = random.choice(resp["default"])
    return bot286_message

# D. Function to interpret user input into chatbot questions
def real(xtext):
    if "name" in xtext:
        ytext = "what's your name?"
    elif "weather" in xtext or "monsoon" in xtext:
        ytext = "what's today's weather?"
    elif "how are" in xtext:
        ytext = "how are you?"
    else:
        ytext = ""
    return ytext

# E. Function to send and receive messages
def send_message(message):
    print(f"You: {message}")
    response = res(message)
    print(f"BOT: {response}")

# F. Loop for interaction
print("BOT: Hi", user_name + "! Ask me something or type 'exit' to quit.")

while True:
    my_input = input().lower()
    if my_input == "exit" or my_input == "stop":
        print("BOT: Goodbye!")
        break
    related_text = real(my_input)
    send_message(related_text)
