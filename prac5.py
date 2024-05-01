class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a chatbot, so I'm always ready to assist you!",
            "bye": "Goodbye! Have a great day!",
            "thank you": "You're welcome!",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return self.responses["default"]


# Example usage:
chatbot = SimpleChatbot()
print("Chatbot: Hi, how can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
