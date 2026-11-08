# mock_model.py
# Author: Jaden Galloway


class MockModel:
    """A stand-on for an AI model. It gives the same simple replies every time."""

    def reply(self, instructions, history):
        """Return a fixed reply based on the last message in the history."""
        last_message = history[-1]["content"].lower()
        if "hello" in last_message:
            return "Hello! How can I help you today?"
        return "I am not sure how to help with that. I can check an order or stock."
