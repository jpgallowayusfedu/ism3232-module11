from my_assistant import CoffeeAssistant
from my_tool import FAQTool


def make_assistant():
    """Build a fresh coffee shop assistant for each test."""
    faqs = {
        "hours": "We are open Monday through Friday from 7:00 am to 6:00 pm.",
        "location": "We are located at 20 Times Square, New York, NY 10036.",
        "menu": "We offer coffee, tea, smoothies, pastries, and breakfast sandwiches",
    }
    return CoffeeAssistant("Amara", FAQTool(faqs))


def test_assistant_greets_user():
    bot = make_assistant()
    assert "Hello" in bot.respond("hello")


def test_assistant_answers_hours_question():
    bot = make_assistant()
    assert "7:00 am to 6:00 pm" in bot.respond("What are your hours?")


def test_assistant_answers_location_question():
    bot = make_assistant()
    assert "20 Times Square" in bot.respond("Where are you located?")


def test_assistant_answers_menu_question():
    bot = make_assistant()
    assert "coffee" in bot.respond("What is on the menu?")


def test_assistant_hands_refund_request_to_human():
    bot = make_assistant()
    assert "human employee" in bot.respond("I want a refund")


def test_assistant_handles_unknown_question():
    bot = make_assistant()
    assert "I am not sure" in bot.respond("Is the sky blue today?")


def test_assistant_records_conversation():
    bot = make_assistant()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"
