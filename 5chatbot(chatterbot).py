# Import necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Step 1: Create a new chatbot
chatbot = ChatBot('Bot286')

# Step 2: Train using a list of custom conversations
list_trainer = ListTrainer(chatbot)

# Sample casual conversation
conversation = [
    'Hi',
    'Hello!',
    'How are you?',
    'I am good, thank you!',
    'What is your name?',
    'I am Bot286, your assistant.',
    'Bye',
    'Goodbye! Have a great day!'
]

list_trainer.train(conversation)

# Step 3: Train using the English corpus
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')

# Step 4: Start conversation with the user
print("Hello! I'm Bot286. Type something to begin a conversation (type 'exit' to stop).")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Bot286: Goodbye! 👋")
        break

    # Get response from the chatbot
    response = chatbot.get_response(user_input)
    print(f"Bot286: {response}")
