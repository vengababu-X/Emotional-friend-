import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

model = whisper.load_model("base")

def listen(seconds=5, filename="input.wav"):
    fs = 16000
    print("Listening...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, recording)
    
    result = model.transcribe(filename)
    return result["text"]
