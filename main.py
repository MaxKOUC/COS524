from engine.tts import speak
from engine.fairytales import get_random_story_text


def run_pipeline():
    """
    Main function for running the pipeline.
    :return:
    """
    # speak("Hello, I am interactive Fairytale Assistant")  # Greeting
    # speak("How can I help you today?")  # Call for action
    # speak("I can tell you a story or answer your questions")  # Self-description

    speak(get_random_story_text())


if __name__ == '__main__':
    run_pipeline()
