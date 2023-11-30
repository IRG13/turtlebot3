import sounddevice as sd
import numpy as np
import wave

CHANNELS = 1
RATE = 44100
DTYPE = np.int16
RECORD_SECONDS = 5
FILENAME = "output.wav"

# Capture audio
audio_data = sd.rec(int(RATE * RECORD_SECONDS), channels=CHANNELS, dtype=DTYPE)
sd.wait()

# Save the audio data to a WAV file
with wave.open(FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio_data.dtype.itemsize)
    wf.setframerate(RATE)
    wf.writeframes(audio_data.tobytes())

print("Recording finished. Audio saved to", FILENAME)
