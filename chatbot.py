# Rule-Based Chatbot

def chatbot():
    print("=" * 50)
    print("Welcome to the Rule-Based Chatbot!")
    print("Type 'exit' to end the conversation.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip().lower()

        # Exit condition
        if user_input == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        # Greetings
        elif user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you today?")

        # Asking chatbot name
        elif "your name" in user_input:
            print("Bot: My name is RuleBot. I am a simple chatbot.")

        # Asking about chatbot
        elif "who are you" in user_input:
            print("Bot: I am a rule-based chatbot developed using Python.")

        # Asking how chatbot is
        elif "how are you" in user_input:
            print("Bot: I'm doing well. Thanks for asking!")

        # Asking time
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {current_time}.")

        # Asking date
        elif "date" in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}.")

        # Asking about Python
        elif "python" in user_input:
            print("Bot: Python is a popular programming language known for its simplicity.")

        # Asking about AI
        elif "artificial intelligence" in user_input or "ai" in user_input:
            print("Bot: Artificial Intelligence enables machines to simulate human intelligence.")

        elif"what is my name?" in user_input :
            print("Bot:your name is prabhas")

        elif"remember my name?" in user_input :
            print("Bot: yes sir your name is prabhas")

        elif"What is my Brother name" in user_input or "brother name" in user_input:
            print("Bot: Your Brother name is DEVA")

        # Asking for help
        elif "help" in user_input:
            print("Bot: You can ask me about my name, AI, Python, date, time, or greetings.")

        # Thank you
        elif "thank you" in user_input or "thanks" in user_input:
            print("Bot: You're welcome!")

        # Default response
        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Start the chatbot
chatbot()