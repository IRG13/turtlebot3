import speech_recognition as sr
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_msgs.msg import Bool
import sounddevice as sd
import numpy as np
import wave
import pygame



class StartBot(Node):

    def __init__(self) -> None:
        super().__init__("StartBot")
         
        # initializes and creates a publisher saying bot has not yet started
        self._pub = self.create_publisher(Bool, 'bot_started', 10)
        self.pub = Bool()

        self.r = sr.Recognizer()
        self.CHANNELS = 1
        self.RATE = 44100
        self.DTYPE = np.int16
        self.RECORD_SECONDS = 10
        self.FILENAME = "/home/maddy/turtlebot3_ws/src/mic_startup/mic_startup/output.wav"

        self._sub = self.create_subscription(Bool, 'bot_started', self.speech_stuff, 10)
        print("Hello")
    def boot(self) -> None:
        self.pub.data = False
        self._pub.publish(self.pub)
    def play_sound(self) -> None:
        pygame.mixer.init()
        sound = pygame.mixer.Sound('/home/maddy/turtlebot3_ws/src/mic_startup/mic_startup/17.wav')
        playing = sound.play()
        while playing.get_busy():
            pygame.time.delay(100)
        pygame.quit()

    def speech_stuff(self, msg: Bool) -> None:
        if msg.data == False:
            self.speech_exporter()
    # if finally, we publish true started
    def speech_exporter(self) -> None:

        audio_data = sd.rec(int(self.RATE * self.RECORD_SECONDS), channels=self.CHANNELS, dtype=self.DTYPE)
        sd.wait()
        with wave.open(self.FILENAME, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(audio_data.dtype.itemsize)
            wf.setframerate(self.RATE)
            wf.writeframes(audio_data.tobytes())

        print("Recording finished. Audio saved to", self.FILENAME)

        with sr.AudioFile(self.FILENAME) as source:
    # listen for the data (load audio to memory)
            audio_data_temp = self.r.record(source)
    # recognize (convert from speech to text)
            if audio_data_temp:
                text = self.r.recognize_google(audio_data_temp)
                print(text)

        if "roll out" in text.lower():
            self.pub.data = True
            self.play_sound()
        elif "rollout" in text.lower():
            self.pub.data = True
            self.play_sound()
        elif "rolls out" in text.lower():
            self.pub.data = True
            self.play_sound()
        elif "roll outs" in text.lower():
            self.pub.data = True
            self.play_sound()
        elif "rolls outs" in text.lower():
            self.pub.data = True
            self.play_sound()
        else:
            self.pub.data = False
        self._pub.publish(self.pub)

def main():
    rclpy.init()
    node = StartBot()
    node.boot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

