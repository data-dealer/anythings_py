# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:55:14 2018

@author: User
"""

import tensorflow as tf
import numpy as np
hello = tf.constant('hello')

sess = tf.Session()

print(sess.run(hello))

# constant la dai luong khong thay doi
x1 = tf.constant(1, name = 'const_1')
x2 = tf.constant(2.)
x3 = tf.constant(3, dtype = 'float32')

v2 = tf.constant([
        [1,2,3], 
        [4,5,6]], dtype = tf.float32, name = '2d_matrix')

v3 = tf.constant([
        [1,1,1], 
        [3,3,2]], dtype = tf.float32, name = '2d_matrix')

sess.run(v2)
v2.eval(session  = sess)


y1 = x2 +x3

y2 = v2 + v3

print(y1)
sess.run(y1)
sess.run(y2)

#-- Placeholder : load du lieu dau vao


p1 = tf.placeholder(dtype = tf.float32)
p2 = tf.placeholder(dtype = tf.float32)

o_add = p1 + p2
o_mul = p1 * p2
o_dental  = p1**2 + p2

# Feel value for placeholder

d_value = {
    p1 : 20,
    p2 : 10        
}
sess.run(o_add, feed_dict= d_value)

sess.run([o_add,o_mul,o_dental], feed_dict= d_value)


#-- Variable

var_1 = tf.Variable( name = 'var1', initial_value= 10)
var_2 = tf.Variable( name = 'var2', initial_value= 50)
# khoi tao tung bien
sess.run(var_1.initializer)

sess.run(var_2)

# khoi tao tat ca cac bien
tf.global_variables_initializer().run(session = sess)

#---- bai toan hoi quy 
#- 1 understanding data
#- 2 preprocessing data  - tien xu ly du lieu
#- 3 feature engineering - trich chon cac dac trung
#- 4 selecting algorithms
#- 5 training
#- 6 fine-tuning         - tinh chinh cac mo hinh 
#- 7 Evaluation          - danh gia mo hinh
#- 8 Deployment          - trien khai thuc te

#------------------------------------------------

# X = [1,2,3,4]  <=> [x0, x1, x2, x3]
# Y = [2]        <=> w_init + w_0 * x0 + .. + w_3 * x3 


# Fake x data
X_data = np.random.random((10000,2)) # 10000 dong , 2 cot

# Fake sample_weights
sample_weights = np.array([3,4]).reshape(2,) # dung de nhan voi X de tao 1 y co nghia

# Fake y_data

Y_data = np.matmul(X_data,sample_weights) # tao ra y co nghia

# Approximation : xap xi hoa 

Y_data = np.add(Y_data, np.random.uniform(-0.5 , 0.5)) # them tinh tuong doi cho y

Y_data = Y_data.reshape(len(Y_data),1) # chuyen y ve 1 cot

from sklearn.model_selection import train_test_split

X_train , X_test, y_train , y_test = train_test_split(X_data , Y_data, test_size = 0.2 , random_state = 42)

X_train.shape
y_train.shape

n_dim =X_train.shape[1]

# placeholder de chuyen du lieu vao
X = tf.placeholder(tf.float32 , [None ,n_dim])
Y = tf.placeholder(tf.float32,[None, 1] )

# cac he so de train weight
W = tf.Variable(tf.ones([n_dim, 1]))
b = tf.Variable(np.random.rand(), dtype = tf.float32)


ped = tf.add(tf.matmul(X,W),b)

loss = tf.reduce_mean(tf.square(ped - Y))
learning_rate = 0.01

optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

#--- Training
sess.run(init)
epochs = 8000
lost_history = []
for epoch in range(epochs):
    sess.run(optimizer , feed_dict = {X: X_train , Y: y_train})

    test_lost = sess.run(loss, feed_dict={X: X_train , Y: y_train})
    lost_history.append(test_lost)
    if epoch % 1000 == 0 :
        print('Epoch : {}  Test loss = {}'.format(epoch, test_lost))
    
sess.run(W)
sess.run(b)


import matplotlib.pyplot as plt

plt.plot(range(len(lost_history)),lost_history)
plt.axis([0, epochs, 0, np.max(lost_history)])
plt.show


