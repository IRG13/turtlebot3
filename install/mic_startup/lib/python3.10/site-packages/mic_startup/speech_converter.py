import speech_recognition as sr
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
import sounddevice as sd
import numpy as np
import wave
from num2words import num2words
from subprocess import call


class startmic(Node):

    def __init__(self) -> None:
        super().__init__("mic_running")
         
        self.r = sr.Recognizer()
        self.CHANNELS = 1
        self.RATE = 44100
        self.DTYPE = np.int16
        self.RECORD_SECONDS = 5
        self.FILENAME = "/home/maddy/turtlebot3_ws/src/mic_startup/mic_startup/output.wav"
        self.responses = {
                     "hello" : "hello there",
                     "hey" : "hey there",
                     "you suck" : "and you swallow",
                     "tell me a joke" : "look into a mirror",
                     }
        
    def play_response(self, key) -> None:
        print(key)
        cmd = f'espeak "{self.responses[key]}" 2>/dev/null -s30'
        call([cmd], shell=True)


    # if finally, we publish true started
    def speech_exporter(self) -> None:

        audio_data = sd.rec(int(self.RATE * self.RECORD_SECONDS), channels=self.CHANNELS, dtype=self.DTYPE)
        sd.wait()
        with wave.open(self.FILENAME, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(audio_data.dtype.itemsize)
            wf.setframerate(self.RATE)
            wf.writeframes(audio_data.tobytes())

        self.get_logger().info("recorded")
        with sr.AudioFile(self.FILENAME) as source:
    # listen for the data (load audio to memory)
            audio_data_temp = self.r.record(source)
    # recognize (convert from speech to text)
            try:
                text = self.r.recognize_google(audio_data_temp)
                self.get_logger().info(text)

            except:
                text = "nah"
        for key in self.responses:
            if key in text.lower():
                self.play_response(key)

def main():
    rclpy.init()
    node = startmic()
    
    while True:
        node.speech_exporter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

