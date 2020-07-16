from random import choice

QUOTES = [
    "Do one thing and do it well.",
    "Action is the foundational key to all success.",
    "Fake it before you make it.",
    "The secret of getting ahead is getting started.",
    "One Day or Day One, you decide.",
    "In the middle of every difficulty lies opportunity.",
    "Focus on being productive instead of busy.",
    "You’re so much stronger than your excuses.",
    "Don't quit.",
    "Be so good they can’t ignore you.",
    "Everything is hard before it is easy.",
]


def get_random_quote(quotes=QUOTES):
    return choice(quotes)
