import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)#数据类型 话题名 缓存几条消息
        self.timer = self.create_timer(1.0, self.timer_callback)#每一秒执行一次
        self.i = 0
        self.subscription = self.create_subscription(String,'topic',self.callback,10)#消息类型 订阅的话题名字 收到消息后执行的函数 消息队列长度
    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, world! {self.i}'
        self.publisher_.publish(msg)
        self.i += 1
        
    def callback(self,msg):
        self.get_logger().info(f'I heard: {msg.data}')

def main():
    rclpy.init()
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
