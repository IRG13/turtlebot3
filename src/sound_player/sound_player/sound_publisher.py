import rclpy
from rclpy.node import Node # To use the Node class

from std_msgs.msg import String # imports the built-in string message type
from std_msgs.msg import Bool

class SoundPublisher(Node): # creates a class that inherits from Node

    def __init__(self):
        super().__init__('sound_publisher') # defines the node name
        # topic name = ‘topic’
        # queue size = 10
        self.publisher_ = self.create_publisher(Bool, '/explore/resume', 10)
        msg = Bool()
        msg.data = True
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data) # published to console

def main(args=None): # main function
    rclpy.init(args=args)
    sound_publisher = SoundPublisher()
    rclpy.spin(sound_publisher) # loops until destroyed
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
    sound_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
