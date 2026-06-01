def get_response(user_input):
    clean_input = user_input.lower().strip()

    # Greetings                 
    if clean_input == "hello" or clean_input == "hi" or clean_input == "hey":
        return "Hey there! I'm Chat. How can I help you today?"

    # How are you
    elif clean_input == "how are you" or clean_input == "how are you?":
        return "I'm perfect! How are you?"
    elif clean_input == "i'm good" or clean_input == "good":
        return "It's good to hear you're doing well. Is there anything i could help you with?"

    # Bot Identity
    elif clean_input == "who are you" or clean_input == "what are you":
        return "I'm Chat, a rule-based AI chatbot."

    # What can you do
    elif clean_input == "what can you do" or clean_input == "help":
        return ("I can respond to:\n"
                "  • Greetings       → hello, hi, hey\n"
                "  • Status          → how are you\n"
                "  • Identity        → who are you\n"
                "  • AI questions    → what is ai, what is ml\n"
                "  • Small talk      → tell me a joke, motivate me\n"
                "  • Farewell        → bye, goodbye\n"
                "  • Exit            → quit / exit")

    # AI knowledge
    elif clean_input == "what is ai" or clean_input == "what is artificial intelligence":
        return "AI (Artificial Intelligence) is the simulation of human intelligence by machines through logic, data, or learning."

    elif clean_input == "what is ml" or clean_input == "what is machine learning":
        return "Machine Learning is a subset of AI where systems learn patterns from data instead of following explicit rules."

    elif clean_input == "what is a chatbot":
        return "A chatbot is a program that simulates conversation. Rule-based bots use logic; AI bots use language models."

    # Small talk
    elif clean_input == "tell me a joke":
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    elif clean_input == "motivate me":
        return "Every expert was once a beginner. The first rule you write today is the foundation of tomorrow's intelligence."

    # Farewell
    elif clean_input == "bye" or clean_input == "goodbye" or clean_input == "see you":
        return "Goodbye!"

    # Empty input
    elif clean_input == "":
        return "Please type something. I'm listening..."

    # Default fallback for unknown inputs
    else:
        return "I don't understand that yet. Type 'help' to see what I can do."

def run_chatbot():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "quit" or user_input.lower().strip() == "exit":
            print("Chat: Session ended. Goodbye!")
            break

        response = get_response(user_input)
        print(f"Chat: {response}")


if __name__ == "__main__":
    run_chatbot() 
