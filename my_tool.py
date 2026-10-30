# my_tool.py
# Author: Jaden Galloway


class FAQTool:
    """A tool that stores and looks up coffee shop information."""

    def __init__(self, faqs):
        self.faqs = faqs

    def find_answer(self, user_message):
        """Find an FAQ answer based on keywords."""
        text = user_message.lower()

        for keyword, answer in self.faqs.items():
            if keyword in text:
                return answer

            if keyword == "location" and "located" in text:
                return answer

        return None
