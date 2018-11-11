## These are codes that are useful when using tensorflow

Determine whether you are using GPU:
```python
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
```
or 
```python
import tensorflow as tf
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
with tf.Session() as sess:
    print (sess.run(c))
```

### use the exact amount of gpu i need
```python
tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
and on the session
sess = tf.Session(graph=detection_graph, config=tfconfig)
```