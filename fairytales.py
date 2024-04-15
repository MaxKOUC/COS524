import os
import random


def get_random_story_text() -> str:
    """
    Get a random story text from fairytales.
    :return:
    """
    stories = os.listdir("./stories")
    story_file = random.choice(stories)
    with open(f"./stories/{story_file}") as f:
        return f.read()
