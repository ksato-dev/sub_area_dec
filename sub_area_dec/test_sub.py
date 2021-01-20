import rclpy
from rclpy.node import Node

# from area_detection_msgs.msg import Result        # CHANGE
import area_detection_msgs  # CHANGE


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber_for_area_dec')
        self.subscription = self.create_subscription(
            # CHANGE
            area_detection_msgs.msg.Data,
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        # self.get_logger().info('I heard: "%d"' % msg.data)  # CHANGE
        self.get_logger().info('I heard: "%d"' % msg.area_name)  # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
