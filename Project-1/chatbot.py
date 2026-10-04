# DecodeLabs - Project 1
# Rule-Based AI Chatbot

print("====================================")
print("      Welcome to AI Chatbot")
print("====================================")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print()

while True:
    user_input = input("You: ").lower().strip()

    # Exit commands
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Greetings
    elif user_input in ["hello", "hi", "hey", "good morning", "good evening"]:
        print("Bot: Hello! How can I help you?")

    # About the chatbot
    elif user_input in ["who are you", "what are you", "your name"]:
        print("Bot: I am a simple rule-based AI chatbot.")

    # How the chatbot is doing
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking.")

    # Help
    elif user_input in ["help", "what can you do"]:
        print("Bot: I can respond to greetings and simple questions.")

    # Thanks
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that yet.")

print("Chatbot session ended.")
