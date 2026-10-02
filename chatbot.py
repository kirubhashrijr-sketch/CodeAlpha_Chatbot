from datetime import datetime


def show_help():
    print("\n🤖 Available Commands:")
    print("1. hello / hi / hey   - Greeting")
    print("2. happy / sad / tired - Mood conversation")
    print("3. time                - Current time")
    print("4. date                - Today's date")
    print("5. about               - About the chatbot")
    print("6. help                - Show commands")
    print("7. bye / exit / quit   - Exit chatbot")
    print()


def chatbot_response(user_input):
    message = user_input.lower().strip()

    # Greetings
    if message in ["hello", "hi", "hey", "good morning",
                   "good afternoon", "good evening"]:
        return "👋 Hello! Nice to meet you! How are you feeling today?"

    # Mood responses
    elif any(word in message for word in
             ["happy", "good", "great", "awesome", "fine"]):
        return "😊 That's great to hear! Keep smiling and have a wonderful day!"

    elif any(word in message for word in
             ["sad", "bad", "upset", "tired"]):
        return "💙 I'm sorry you're feeling that way. Take some rest and stay positive!"

    elif "how are you" in message:
        return "🤖 I'm doing great! Thanks for asking!"

    # Time
    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"🕐 The current time is {current_time}."

    # Date
    elif "date" in message or "today" in message:
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"📅 Today's date is {current_date}."

    # About bot
    elif message == "about" or "who are you" in message:
        return (
            "🤖 I'm CodeAlpha Basic Chatbot. "
            "I'm a Python-based chatbot that can handle "
            "greetings, moods, time, date, help, and exit commands."
        )

    # Help
    elif message in ["help", "commands", "options"]:
        show_help()
        return None

    # Exit
    elif message in ["bye", "exit", "quit", "goodbye"]:
        return "👋 Goodbye! Thanks for chatting with me. Have a great day!"

    # Unknown input
    else:
        return "🤔 I didn't understand that. Type 'help' to see what I can do."


def main():
    print("=" * 55)
    print("             CODEALPHA BASIC CHATBOT")
    print("=" * 55)
    print("🤖 Hello! I'm your Python chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("=" * 55)

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        if response:
            print("Bot:", response)

        if user_input.lower().strip() in [
            "bye", "exit", "quit", "goodbye"
        ]:
            break


if __name__ == "__main__":
    main()