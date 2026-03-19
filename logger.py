def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a") as file:
        file.write(f"User: {user_input}\n")
        file.write(f"Bot: {bot_response}\n")
        file.write("-" * 40 + "\n")