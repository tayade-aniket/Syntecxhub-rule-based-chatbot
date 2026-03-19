import re
from knowledge_base import knowledge_base

class ChatBot:

    def __init__(self):
        self.intents = {
            "greeting": ["hi", "hello", "hey"],
            "help": ["help", "assist", "support"],
            "bye": ["bye", "exit", "quit"],
            "smalltalk": ["how are you", "what's up"]
        }

    def match_intent(self, user_input):

        user_input = user_input.lower()

        for intent, patterns in self.intents.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    return intent

        return None

    def get_response(self, user_input):

        user_input = user_input.lower()

        # 1. Check knowledge base
        if user_input in knowledge_base:
            return knowledge_base[user_input]

        # 2. Match intents
        intent = self.match_intent(user_input)

        if intent == "greeting":
            return "Hello! How can I help you today?"

        elif intent == "help":
            return "I can answer basic AI questions or chat with you."

        elif intent == "smalltalk":
            return "I'm just a bot, but I'm doing great! How about you?"

        elif intent == "bye":
            return "Goodbye! Have a nice day."

        # 3. Default fallback
        return "Sorry, I don't understand that yet."