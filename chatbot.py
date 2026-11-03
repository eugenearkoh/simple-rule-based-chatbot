import re
from datetime import datetime


class ObedAI:

    def __init__(self):
        self.name = "OBED AI"
        self.user_name = None

    # Clean and process user input
    def clean_input(self, message):
        message = message.lower().strip()
        message = re.sub(r"[^\w\s']", "", message)
        message = re.sub(r"\s+", " ", message)
        return message

    # Generate chatbot responses
    def get_response(self, user_input):

        message = self.clean_input(user_input)

        if not message:
            return "Please enter a message so I can assist you."

        # English greetings
        if any(word in message.split() for word in
               ["hello", "hi", "hey", "good morning",
                "good afternoon", "good evening"]):
            return "Hello! Welcome to OBED AI. How can I help you today?"

        # Twi greetings
        if "maakye" in message:
            return "Maakye! Wo ho te sɛn? Welcome to OBED AI!"

        if "maaha" in message:
            return "Maaha! Wo ho te sɛn?"

        if "maadwo" in message:
            return "Maadwo! Ɛte sɛn?"

        if "wo ho te sen" in message:
            return "Me ho yɛ! Medaase. Na wo nso ɛ?"

        if "medaase" in message or "medaase pii" in message:
            return "Yoo! You're welcome. Always happy to help!"

        if "akwaaba" in message:
            return "Medaase! Akwaaba to OBED AI!"

        # Introductions
        if "what is your name" in message or "who are you" in message:
            return "I am OBED AI, your personal virtual assistant, proudly inspired by Ghana!"

        # User introduction
        if message.startswith("my name is "):
            self.user_name = user_input.strip()[11:].strip().title()

            return f"Nice to meet you, {self.user_name}! I'm OBED AI."

        # Identity
        if "who created you" in message or "who made you" in message:
            return "I am OBED AI, a Python-based rule-driven chatbot created as a learning project."

        # Capabilities
        if "help" in message or "what can you do" in message:
            return (
                "I can respond to greetings, recognize some Twi expressions, "
                "answer basic questions, tell you the date and time, "
                "and chat with you."
            )

        # Date and time
        if "time" in message:
            return f"The current time is {datetime.now().strftime('%I:%M %p')}."

        if "date" in message or "today" in message:
            return f"Today is {datetime.now().strftime('%A, %d %B %Y')}."

        # Ghanaian identity
        if "ghana" in message or "ghanaian" in message:
            return "Akwaaba! 🇬🇭 OBED AI proudly embraces Ghanaian culture and conversations."

        # Artificial intelligence
        if "artificial intelligence" in message or "what is ai" in message:
            return (
                "Artificial Intelligence (AI) is technology that enables "
                "machines to perform tasks that normally require human intelligence."
            )

        # Programming
        if "python" in message:
            return (
                "Python is a popular programming language used in "
                "artificial intelligence, automation, web development and data science."
            )

        # Appreciation
        if "thank you" in message or "thanks" in message:
            return "You're welcome! I'm always happy to assist you."

        # Goodbye
        if any(word in message.split() for word in
               ["bye", "goodbye", "exit", "quit"]):
            return "Medase! Thank you for chatting with OBED AI. Goodbye!"

        # Fallback response
        return (
            "I'm still learning! I don't understand that message yet. "
            "Try asking me something else or type 'help' to see what I can do."
        )


# Simple terminal conversation
if __name__ == "__main__":

    chatbot = ObedAI()

    print("\n================================")
    print("       WELCOME TO OBED AI")
    print("================================")
    print("Your Personal Virtual Assistant 🇬🇭")
    print("Type 'exit' to end the conversation.\n")

    while True:

        user_message = input("You: ")

        response = chatbot.get_response(user_message)

        print(f"OBED AI: {response}\n")

        if chatbot.clean_input(user_message) in ["exit", "quit", "bye", "goodbye"]:
            break
