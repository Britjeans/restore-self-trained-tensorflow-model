import tensorflow as tf
import numpy as np
import cv2
from model.Alex import AlexNet
import tensorflow as tf
from readdata import readimg

NUM_CLASSES=2
IMAGE_SIZE=227


# read image
img=None
for i in range(1,6):
    im = readimg('test/violent/' + str(i))
    if img==None:
        img=[im]
    else:
        img=np.append(img,[im],axis=0)


x = tf.placeholder(tf.float32, [ 5,IMAGE_SIZE, IMAGE_SIZE, 20])

# initialization
model = AlexNet(x, NUM_CLASSES)
score = model.fc8



with tf.name_scope('result')as scope:
    result=tf.argmax(tf.nn.softmax(score), 1)


saver=tf.train.Saver()

with tf.Session() as sess:
    #notice the order of initialize_all_variables and restore weights from checkpoint
    sess.run(tf.global_variables_initializer())
    # restore saved weights
    ckpt = tf.train.get_checkpoint_state('check')
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        print("failed!")
    all_vars = tf.get_collection('vars')
    print ('test saved network:')
    predict=sess.run(result,feed_dict={x:img})
    print(predict)
