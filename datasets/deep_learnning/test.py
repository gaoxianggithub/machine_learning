import tensorflow as tf
# 获取gpu列表
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
print(gpus)