# my_main.py
# Author: Jaden Galloway

from my_assistant import CoffeeAssistant
from my_tool import FAQTool

FAQS = {
    "hours": "We are open Monday through Friday from 7:00 am to 6:00 pm.",
    "location": "We are located at 20 Times Square, New York, NY 10036.",
    "menu": "We offer coffee, tea, smoothies, pastries, and breakfast sandwiches",
}

faq_tool = FAQTool(FAQS)

bot = CoffeeAssistant("Amara", faq_tool)
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
