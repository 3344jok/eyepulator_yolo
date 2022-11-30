# eyepulator_yolo

## 安装yolo环境(本人使用的是conda虚拟环境)

```sh
参照yolo官方readme安装环境
此外还需要安装rospkg:pip install rospkg
```

## 安装web-video-server,并编写launch文件，参照谷歌

```sh
sudo apt-get install ros-kinetic-web-video-server
roscd web_video_server
mkdir launch
cd launch
sudo gedit web_video.launch
web_video.launch中的内容如下
<launch>
  <node pkg="web_video_server" type="web_video_server" name="web_video_server_1" output="screen">
    <param name="port" type="int" value="8080" />
    <param name="address" type="string" value="127.0.0.1" />
    <param name="server_threads" type="int" value="1" />
    <param name="ros_threads" type="string" value="2" />

    <param name="quality" type="int" value="100" />
    <param name="default_transport" type="string" value="raw" />
    <param name="type" type="string" value="png" />

  </node>
</launch>    
```

## 启动web-video-server(roslaunch会自动启动一个ros-master)

```sh
roslaunch web_video_server web_video.launch 
```

## 启动rosbag发布话题

```sh
rosbag play apriltagCar.bag
```

## yolo检测话题发布的图像序列

```sh 
python detect.py --source 'http://127.0.0.1:8080/stream?topic=/camera_ir/rgb/image_raw' --weights runs/aCar_weights/exp13/weights/best.pt --data data/aCar.yaml 
- source 图像序列的url:'http://127.0.0.1:8080/stream?topic=ros话题'
- weights 网络权重
```

## 结束检测

- 直接 ctrl+c 关闭web-video-server进程
