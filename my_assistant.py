# my_assistant.py
# Author: Jaden Galloway


class CoffeeAssistant:
    """A coffee shop assistant that uses rules, an FAQ tool, and an AI model."""

    def __init__(self, faq_tool, instructions, model):
        """Set up the FAQ tool, instructions, model, and conversation history."""
        self.faq_tool = faq_tool
        self.instructions = instructions
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the conversation and return the assistant's response."""
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def choose_reply(self, user_message):
        """Use a rule or FAQ answer first. Otherwise ask the model."""
        text = user_message.lower()

        if "refund" in text or "complaint" in text:
            return "I can't handle that here. I am passing you to a human employee"

        answer = self.faq_tool.find_answer(user_message)

        if answer is not None:
            return answer

        return self.model_reply()

    def model_reply(self):
        """Ask the model for an answer or return a safe message."""
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."

        return reply
