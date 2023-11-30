import rclpy 
from rclpy.node import Node 
from std_msgs.msg import Bool 
import importlib.machinery
import importlib.util

# Import mymodule
loader = importlib.machinery.SourceFileLoader( 'player', '/home/maddy/turtlebot3_ws/src/sound_player/sound_player/player.py' )
spec = importlib.util.spec_from_loader( 'player', loader )
player = importlib.util.module_from_spec( spec )
loader.exec_module( player )

#subscribes to /video0 and publishes to /shoe_detected

class ShoeDetectorNode(Node):
    
    def __init__(self) -> None:
        super().__init__("soundplayer_node")
        # Check if non-footwear wearing people in topic /detected
        self._sub = self.create_subscription(
            Bool, "shoe_detected", self.detected, 10
	        )

    def detected(self, msg):
        if msg.data == False:
            player.run()

def main():
    rclpy.init()
    node = ShoeDetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
