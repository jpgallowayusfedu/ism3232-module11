# my_assistant.py
# Author: Jaden Galloway


class CoffeeAssistant:
    """A mock assistant for a fictional coffee shop."""

    def __init__(self, name, faq_tool):
        """Set up the assistant for a fictional coffee shop."""
        self.name = name
        self.faq_tool = faq_tool
        self.history = []

    def respond(self, user_message):
        """Record the message, choose a reply, and record the response."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply based on simply keyword rules."""
        text = user_message.lower()

        if "refund" in text or "complaint" in text:
            return "I can't handle that here. I am passing you to a human employee"

        answer = self.faq_tool.find_answer(user_message)

        if answer is not None:
            return answer

        if "hello" in text:
            return "Hello! I'm Amara! I can answer questions about our coffee shop. How can I help you today?"

        return "I am not sure how to help with that. I can answer questions about other aspects of our coffee shop."
