# kafka_tools
## 支持简单的kafka连接检测以及简单发送、接收测试
## 不支持带验证的kafka！！！
> 如果希望同时连接、发送，可以选择启动两个脚本  
mac版本无法同时启动两个，可以右键项目，选择查看包内容，在MACOS目录下有一个main_support，双击后可以启动第二个

## 使用方法：
1. 打开软件
2. 设置好kafka的ip（必填）、port（必填）、topic（必填），生产者可以不写groupid
3. 保存
4. 【生产信息】：最下方输入框输入信息，点击发送消息，如果卡住了，等待1分钟左右会有具体错误，一般都是kafka有问题
5. 【消费信息】：直接点击启动消费者，等待启动成功，如果kafka有问题或topic不存在，则会提示异常
## 不会打包使用？  
    如果项目不会使用，可以直接下载kafka tools v1.0目录下的指定版本文件
    
## 软件截图
![](https://img-blog.csdnimg.cn/20210207143122261.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2hoZjc5OTk1NDc3Mg==,size_16,color_FFFFFF,t_70#pic_center)


> 更新日志
> 2021-01-28
> 1. 项目上传github
> 2. 修改项目的一些内容
> 2021-02-07
> 1. 增加了刷新列表的功能
> 2. 增加github链接
> 2021-02-07
> 1. 消费的数据可有选择的进行持久化

各位同行可以提出建设性的issues或者一起开发，欢迎star，欢迎pr
