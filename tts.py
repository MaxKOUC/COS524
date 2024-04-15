import pyttsx3
import torch
engine = pyttsx3.init()


def speak(text: str) -> None:
    tts = TTS("CHOSEN/MODEL/NAME")
    tts.tts_to_file(text="Hello World", output_path="PATH/TO/OUTPUT.wav")

    if not text:
        return
    engine.say(text)
    engine.runAndWait()


from TTS.api import TTS
from TTS.utils.synthesizer import Synthesizer
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
synthesizer = Synthesizer("tts_models/multilingual/multi-dataset/xtts_v2", "tts_models/multilingual/multi-dataset/xtts_v2")

synthesizer.tts("Hello World")
