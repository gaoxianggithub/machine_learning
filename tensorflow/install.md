# tensorflow学习
## 1.搭建环境

[1.1 安装](#1.1 环境说明)



### 1.1 环境说明
* **CPU**: amd R7-5800x
* **GPU**: amd RX-6600xt

* **系统**：windows11
* **python**: 3.10
* **conda**:  23.1.0

## 1.2 安装

1. 安装amd驱动

打开[官网](https://www.amd.com/en/support)选择合适的驱动，本机是RX-6600xt 

![image-20230328104652224](https://gitee.com/shawn2gao/myimg/raw/master/markdown/2023-03/image-20230328104652224.png)

`下载驱动安装完成后重启电脑`

2. 使用conda（或者pip）安装tensorflow

```sh
# 1.安装tensorflow
# conda
conda installl tensorflow
# pip
pip installl tensorflow
# 2.安装tensorflow-directml-plugin, 我安装的时候，conda没有这个包，所有此处只有pip
pip install tensorflow-directml-plugin
```

3. 测试是否安装完成，安装成功后会显示以下参数，至此，安装完毕

```python
import tensorflow as tf
print(tf.__version__)

with tf.device('cpu'):
    a = tf.constant([1])
    print(a.device)
 
with tf.device('gpu'):
    b = tf.constant([1])
    print(b.device)
# 控制台分别打印：
# 2.10.0
# /job:localhost/replica:0/task:0/device:CPU:0
# /job:localhost/replica:0/task:0/device:GPU:0
```

