import rclpy
from rclpy.node import Node

from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup

from std_msgs.msg import String

import time


class RobotNode(Node):
    """机器人节点"""
    def __init__(self):
        super().__init__("robot_node")
        self.callback_group = ReentrantCallbackGroup()  # 创建一个回调组
        self.timer = self.create_timer(
            1.0,
            self.control_callback,
            callback_group=self.callback_group
        )

        self.subscription = self.create_subscription(
            String,
            "sensor",
            self.sensor_callback,
            10,
            callback_group=self.callback_group
        )

    def control_callback(self):
        """节点控制回调"""
        self.get_logger().info(
            "控制电机"
        )

        time.sleep(3)

        self.get_logger().info(
            "电机控制完成"
        )

    # 另一个任务
    def sensor_callback(self,msg):
        """传感器数据回调"""
        self.get_logger().info(
            "收到传感器:" + msg.data
        )



def main():

    rclpy.init()
    node = RobotNode()

    # 创建多线程执行器
    executor = MultiThreadedExecutor(num_threads=2)
    executor.add_node(node)
    executor.spin()
    node.destroy_node()
    rclpy.shutdown()

