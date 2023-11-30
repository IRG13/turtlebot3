import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import pygame
from random import choice

pygame.init()

#subscribes to /video0 and publishes to /shoe_detected

class ShoeDetectorNode(Node):
    
    def __init__(self) -> None:
        super().__init__("soundplayer_node")

        # Check if non-footwear wearing people in topic /detected
        self._sub = self.create_subscription(
            Bool, "shoe_detected", self.detected, 10
        )

        # List of audio files to be played
        self.path = '~/turtlebot3_ws/src/sound_player/cursed-sounds/'
        self.alerts = [
            self.path + '1.wav',
            self.path + '2.wav',
            self.path + '3.wav',
            self.path + '4.wav',
            self.path + '5.wav',
            self.path + '6.wav',
        ]

    def detected(self, msg):
        if msg.data == True:
            self.play_sound

    def play_sound(self) -> None:
        file = choice(self.alerts)
        alert = pygame.mixer.Sound(file)
        alert.play()
    
def main():
    rclpy.init()
    node = ShoeDetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
