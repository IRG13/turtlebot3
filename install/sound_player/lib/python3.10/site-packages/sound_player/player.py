"""OpenAL playback example."""
import os
import sys
import time
import wave
from openal import al, alc
from random import choice

def run():

    path = "/home/maddy/turtlebot3_ws/src/sound_player/cursed-sounds/"
    alerts = [path + '1.wav',
              path + '2.wav',
              path + '3.wav',
              path + '4.wav',
              path + '5.wav',
              path + '6.wav',
              path + '7.wav',
              path + '8.wav',
              path + '9.wav',
              path + '10.wav',
              path + '11.wav',
              path + '12.wav',
              path + '13.wav',
              path + '14.wav',
              path + '15.wav',
              path + '16.wav',
              path + '17.wav',
              path + '18.wav',
              path + '19.wav',
              path + '20.wav',
              path + '21.wav',
              path + '22.wav',
              path + '23.wav',
              path + '24.wav',
              path + '25.wav',
]
    fname = choice(alerts)
    wavefp = wave.open(fname)
    channels = wavefp.getnchannels()
    bitrate = wavefp.getsampwidth() * 8
    samplerate = wavefp.getframerate()
    wavbuf = wavefp.readframes(wavefp.getnframes())
    formatmap = {
        (1, 8) : al.AL_FORMAT_MONO8,
        (2, 8) : al.AL_FORMAT_STEREO8,
        (1, 16): al.AL_FORMAT_MONO16,
        (2, 16) : al.AL_FORMAT_STEREO16,
    }
    alformat = formatmap[(channels, bitrate)]

    device = alc.alcOpenDevice(None)
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    source = al.ALuint(0)
    al.alGenSources(1, source)

    al.alSourcef(source, al.AL_PITCH, 1)
    al.alSourcef(source, al.AL_GAIN, 1)
    al.alSource3f(source, al.AL_POSITION, 10, 0, 0)
    al.alSource3f(source, al.AL_VELOCITY, 0, 0, 0)
    al.alSourcei(source, al.AL_LOOPING, 1)

    buf = al.ALuint(0)
    al.alGenBuffers(1, buf)

    al.alBufferData(buf, alformat, wavbuf, len(wavbuf), samplerate)
    al.alSourceQueueBuffers(source, 1, buf)
    al.alSourcePlay(source)

    state = al.ALint(0)
    al.alGetSourcei(source, al.AL_SOURCE_STATE, state)
    z = 10
    while z > 4:
        time.sleep(1)
        al.alSource3f(source, al.AL_POSITION, 0, 0, 0)
        z -= 1

    al.alDeleteSources(1, source)
    al.alDeleteBuffers(1, buf)
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)

if __name__ == "__main__":
    sys.exit(run())
