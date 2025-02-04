# 第二次任务
**学习目标**
> 1. 阐述ros架构以及话题节点服务等之间的通信关系
> 2. 动手编写一个listener和publisher，发布信息 为welcome to RM！
> 3. 提供rqt截图
## 1.ros架构
根据<https://fishros.com/d2lros2/#/humble/chapt1/advanced/1.ROS2%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84>
### 1. 架构图
![ros](https://fishros.com/d2lros2/humble/chapt1/advanced/1.ROS2%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84/imgs/image-20220602204152352.png)

### 2. 操作系统层

    ROS2本身就是基于Linux、Windows或者macOS系统建立的，驱动计算机硬件、底层网络通信等实现都是交由操作系统来实现的
### 3. DDS实现层  
    * DDS，全称 Data Distribution Service (数据分发服务)。是由对象管理组 (OMG) 于 2003 年发布并于 2007 年修订的开分布式系统标准。
    * 通过类似于ROS中的话题发布和订阅形式来进行通信，同时提供了丰富的服务质量管理来保证可靠性、持久性、传输设置等。
    * DDS实现层其实就是对不同常见的DDS接口进行再次的封装，让其保持统一性，为DDS抽象层提供统一的API。
### 4. 抽象DDS层-RMW  
    这一层将DDS实现层进一步的封装，使得DDS更容易使用。原因在于DDS需要大量的设置和配置（分区，主题名称，发现模式，消息创建,...），这些设置都是在ROS2的抽象层中完成的。
### 5. ROS2客户端库 RCL

    RCL（ROS Client Library）ROS客户端库，其实就是ROS的一种API，提供了对ROS话题、服务、参数、Action等接口。
    * GUI（Graphical User Interface）就是平常我们说的图形用户界面
    * CLI（Command-Line Interface）就是命令行界面了，我们所用的终端，黑框框就是命令行界面，没有图形化。
    * API（ Application Programming Interface）应用程序编程接口。在c中表现为头文件。  

    ROS的客户端库就是上面所说的RCL，不同的语言对应着不同的rcl，但基本功能都是相同的。

    比如Python语言提供了rclpy来操作ROS2的节点话题服务等，而C++则使用rclcpp提供API操作ROS2的节点话题和服务等。

    所以后面我们使用Python和C++来编写ROS2节点实现通讯等功能时，我们就会引入rclpy和rclcpp的库。 
### 6. 应用层

    应用层就是我们写代码以及ROS2开发的各种常用的机器人相关开发工具所在的层了。后面我们写的所有代码其实都是属于这一层的。
***
## 2. ROS2节点通信之话题与服务
### 通信的目的

通信的目的是在计算机系统中实现不同组件、进程或设备之间的信息和数据传递。通过通信，各个实体可以共享信息、协调行动并实现协同工作。在计算机领域，通信是构建分布式系统、网络和协议的基础。
### 通信原理

通信的原理涉及两个主要方面：通信协议和通信方式。通信协议定义了数据的格式、传输方式、错误检测和纠正等规则，以确保可靠的数据传输。通信方式涉及了不同的通信介质和技术，包括网络通信和进程间通信（IPC）。
### 通信方式
1. 基于TCP/UDP的网络通信方式

基于TCP/UDP的网络通信方式通过计算机网络进行信息交换。其中，TCP（传输控制协议）提供可靠的、面向连接的通信，而UDP（用户数据报协议）则是无连接的通信方式。在Linux命令行中，可以使用诸如ping和nc命令来演示网络通信。

例如，使用ping命令进行基于UDP的网络通信：

    ping 192.168.0.1

该命令将向IP地址为192.168.0.1的主机发送ICMP Echo请求，并等待接收相应的回复。

使用nc命令进行基于TCP的网络通信：

    nc -l 1234

该命令将在本地监听端口1234，并等待与之建立TCP连接的客户端。通过在另一个终端窗口中执行以下命令，可以建立与本地1234端口的TCP连接并在连接上发送消息：

    echo "Hello, TCP!" | nc 127.0.0.1 1234
2. 基于共享内存的进程间通信（IPC）方式

基于共享内存的IPC方式通过共享内存区域在同一计算机系统内的不同进程之间进行通信。在Linux命令行中，可以使用ipcs和ipcrm命令来管理共享内存段。

通过ipcs命令查看当前系统中的共享内存段：

    ipcs -m

使用ipcrm命令删除不再需要的共享内存段：

    ipcrm -m <shmid>
### 话题入门
#### 1. 订阅发布模型

一个节点发布数据到某个话题上，另外一个节点就可以通过订阅话题拿到数据。
![alt text](image.png)
除了上述这种一个节点发布，一个节点接受的形式外，ROS2话题通信其实还可以是1对n,n对1,n对n的。
* 还有一种就是ROS2节点可以订阅本身发布的话题
![alt text](image-1.png)
#### 2. 消息接口

为了方便发送者和接收者进行数据的交换，ROS2帮我们在数据传递时做好了消息的序列化和反序列化.而且ROS2的消息序列化与反序列化通信是可以做到跨编程语言、跨平台和跨设备之间的。  
当我们定义好消息接口后，ROS2会根据消息接口内容生成不同语言的接口类，在不同编程语言中调用相同的类即可实现无感的消息序列化和反序列化。  
通过对消息接口介绍，相信你肯定能猜到这样一条规则：同一个话题，所有的发布者和接收者必须使用相同消息接口。
#### 3. ROS2话题工具
##### 3.1 GUI工具
3.1.1 RQT工具之rqt_graph

ROS2作为一个强大的工具，在运行过程中，我们是可以通过命令来看到节点和节点之间的数据关系的。  

    ros2 run demo_nodes_py listener
    ros2 run demo_nodes_cpp talker
    rqt_graph
可以看到图片
![alt text](image-2.png)
#### 3.2 CLI工具
**用`ros2 topic -h`查看**

3.2.1  `ros2 topic list` 返回系统中当前活动的所有主题的列表
***
3.2.2 `ros2 topic list -t` 增加消息类型
***
3.2.3 `ros2 topic echo` 打印实时话题内容  

    ros2 topic echo /chatter
***
3.2,4 `ros2 topic info` 查看主题信息  

    ros2 topic info  /chatter
![alt text](image-3.png)
***
3.2.5 `ros2 interface show` 查看消息类型  

上面一个指令告诉大家这个消息是std_msgs/msg/String，那String里面有什么呢？  

    ros2 interface show std_msgs/msg/String
***
3.2.6 ros2 topic pub arg 手动发布命令

    ros2 topic pub /chatter std_msgs/msg/String 'data: "123"'
### 话题之rclcpp实现
### 1.创建节点
本节我们将创建一个`控制节点`和一个`被控节点`。