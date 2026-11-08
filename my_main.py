# my_main.py
# Author: Jaden Galloway

from my_assistant import CoffeeAssistant
from my_tool import FAQTool
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Amara, a friendly coffee shop assistant.
The coffee shop is open Monday through Friday from 7:00 am to 6:00 pm.
The coffee shop is located at 20 Times Square, New York, NY 10036.
The coffee shop serves coffee, tea, smoothies, pastries, and breakfast sandwiches.
If you do not know an answer, say you do not know and offer human assistance.
Answer in one short sentence.
Only state facts included in these instructions."""

faq_tool = FAQTool(
    {
        "hours": "We are open Monday through Friday from 7:00 am to 6:00 pm.",
        "location": "We are located at 20 Times Square, New York, NY 10036.",
        "serves": "We offer coffee, tea, smoothies, pastries, and breakfast sandwiches.",
    }
)
model = OllamaModel(MODEL_NAME)

bot = CoffeeAssistant(faq_tool, INSTRUCTIONS, model)

print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"Amara: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
