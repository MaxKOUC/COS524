import pyaudio
from threading import Thread
from queue import Queue
import subprocess
import json
from vosk import Model, KaldiRecognizer
import time

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

model = Model(model_name="vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)


messages = Queue()
recordings = Queue()


def speech_recognition(output):
    while not messages.empty():
        print("process message")
        frames = recordings.get()

        rec.AcceptWaveform(b''.join(frames))
        result = rec.Result()
        text = json.loads(result)["text"]

        #cased = subprocess.check_output('python recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True, text=True, input=text)
        #output.append_stdout(cased)
        print(text)
        time.sleep(1)


def record_microphone(chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=AUDIO_FORMAT,
        channels=CHANNELS,
        rate=FRAME_RATE,
        input=True,
        input_device_index=18,
        frames_per_buffer=chunk
    )

    frames = []

    while not messages.empty():
        data = stream.read(chunk)
        frames.append(data)
        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
            recordings.put(frames.copy())
            frames = []
    stream.stop_stream()
    stream.close()
    p.terminate()


#record = Thread(target=record_microphone)
#transcribe = Thread(target=speech_recognition)

#record.start()
#transcribe.start()

#time.sleep(35)

#record.join()
#transcribe.join()
