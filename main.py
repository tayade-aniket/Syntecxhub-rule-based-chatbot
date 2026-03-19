from chatbot import ChatBot
from logger import log_conversation

def main():

    bot = ChatBot()

    print("=== Rule-Based Chatbot ===")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break

        response = bot.get_response(user_input)

        print("Bot:", response)

        log_conversation(user_input, response)


if __name__ == "__main__":
    main()