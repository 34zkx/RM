#   节点
## py 节点
    import rclpy
    from rclpy.node import Node
    def main ():
        rclpy.init()#初始化
        node = Node('python_node')##创建节点
        node.get_logger().info('nihao python')
        node.get_logger().warn('nihao python')
        rclpy.spin(node)#运行
        rclpy.shutdown()#关闭节点
    if __name__=='__main__':
        main()

## c++ 节点
    #include "rclcpp/rclcpp.hpp"

    int main(int argc,char** argv)
    {
        rclcpp::init(argc,argv);
        auto node = std::make_shared<rclcpp::Node>("cpp_node");
        RCLCPP_INFO(node->get_logger(),"hello c++node");
        rclcpp::spin(node);
        rclcpp::shutdown();
        return 0;
    }
### cmake
    cmake_minimum_required(VERSION 3.8)
    project(ros2cpp)
    add_executable(ros2_cpp_node ros2_cpp_node.cpp)

    find_package(rclcpp REQUIRED) #查找头文件和库文件
    message(STATUS ${rclcpp_INCLUDE_DIRS})#头文件及rclcpp依赖头文件
    message(STATUS ${rclcpp_LIBRARIES})#   库文件及rclcpp依赖库
    target_include_directories(ros2_cpp_node PUBLIC ${rclcpp_INCLUDE_DIRS})#头文件包含
    target_link_libraries(ros2_cpp_node ${rclcpp_LIBRARIES})#库文件链接
## 功能包组织py节点
`ros2 pkg create 功能包名字--类型 ament_python --证书` #创建功能包

示例 `ros2 pkg create demo_pythn_pkg --build-type ament_python --license Apache-2.0`

在`demo_python_pkg/demo_python_pkg`目录下新建`python_node.py`

打开`demo_python_pkg/package.xml`,添加依赖（可不做）

构建`colcon build`

`source install/setup.bash`更改环境变量
### 注意
构建包，设置环境后还要对setup.py文件修改

    from setuptools import setup

    setup(
        # ... 其他设置 ...
        entry_points={
            'console_scripts': [
                'talker = my_python_pkg.talker:main',  # 如果已经有 talker，确保它也正确
                'listener = my_python_pkg.listener:main'  # 添加这一行或确保它存在且正确
            ],
        },
    )
'talker = my_python_pkg.talker:main'  
与  
'listener = my_python_pkg.listener:main'  
中间用逗号隔开！！

