import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GPSOdomReversePublisher(Node):

    def __init__(self):
        super().__init__('gps_odom_reverse_publisher')
        self.publisher_ = self.create_publisher(String, 'gps_odom_reverse', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, this is a GPS Odom Reverse message'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = GPSOdomReversePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()