import re

responses = {
    r'hi|hello|hey':"Hello how can i assist you",
    r'what.*your name': "I am a customer service chatbot",
    r'how.*you': "i am just a bot , i am here to help",
    r'what time.*open|hour': "Our store is open from 9 am to 9pm everyday",
    r'where.*located': "Our store is located in pune",
    r'do you have.*': "let me check,could you specify model",
    r'bye|goodbye': "Goodbye! Have a great day",
}

def chatbot_response(user_input):
    for pattern , response in responses.items():
        if re.search(pattern , user_input , re.IGNORECASE):
            return response
    return "I am sorry , i did not understand that ,can you rephase?"

print("Customer Support Bot: Hello! How can I help you today? (Type 'exit' to quit)")

while True:
    user_input = input("you: ")
    if user_input.lower() == "exit":
        print("Customer Support Bot: Thank you for chatting! Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Customer Support Bot: {response}")
