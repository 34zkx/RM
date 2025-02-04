import rclpy
from rclpy.node import Node
def main ():
    rclpy.init()#初始化
    node = Node('python_node')##创建节点
    node.get_logger().info('nihao python')
    node.get_logger().warn('nihao python')
    rclpy.spin(node)#运行
    rclpy.shutdown()#关闭节点

