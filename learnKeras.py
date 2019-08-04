

from keras.models import Sequential
from keras.layers import Dense, Activation

# khai bao model 
model = Sequential([
    Dense(4,input_shape = (3,)),
    Dense(2)
])

model.summary()



""" De bai --------------------------------------lession 3
cho phương trinh y = wx + b  (y = ax + b)
- cho nghiệm x = [x1, x2, x3, ... xn] , y = [y1, y2, y3, ... yn]
- tìm w
"""
from keras.models import *
from keras.layers import *
from keras import optimizers
x = [1,2,3,4] 
y = [2,4,6,8]


model = Sequential([
    Dense(1,input_shape = (1,)),
])

model.summary()

# train model

sgd = optimizers.SGD(lr = 0.01)

model.compile( loss = 'mse', optimizer = sgd)

model.fit(x,y,epochs = 1500)

# du doan
y_pred = model.predict([7,])
y_pred

""" --------------------------------------lession 4 training nhiều đầu vào tuyến tính
cho phương trinh y = wx + b  (y = ax + b)
- cho nghiệm x = [x1, x2, x3, ... xn] , y = [y1, y2, y3, ... yn]
- tìm w
"""
from keras.models import *
from keras.layers import *
from keras import optimizers
import numpy as np
import pandas as pd
x_data =[[73,89,75],
          [93,88,93],
          [89,91,90],
          [96,98,100],
          [73,66,70]]

y_data = [[152],
          [185],
          [180],
          [196],
          [142]]

x_data = np.asarray(x_data)
y_data = np.asarray(y_data)

#--------------load tu csv
xy = np.loadtxt('b4.csv', delimiter = ',')
x_data = xy[: , 0:-1]
y_data = xy[: , [-1]]


model_2 = Sequential()

model_2.add(Dense(units = 3, input_dim = 3))
#model_2.add(Dense(units = 3))
#model_2.add(Dense(units = 2))
model_2.add(Dense(units = 1))
# co them lop



model_2.compile(loss = 'mse' , optimizer= 'rmsprop')

model_2.summary()
model_2.fit(x_data,y_data,epochs = 20000)

model_2.predict(np.array([[82,86,90]]))

#------------Save model -----------------
model_2.save('trained_model.h5')


#---------- Load model ---------------
from keras.models import load_model
model = load_model('trained_model.h5')

model.predict(np.array([[82,86,90]]))

# dung numpy:

a = np.arange(10)
b = np.arange(10,25,5)
c = np.linspace(0,2,5)
a.shape
len(a)
a.ndim # so chieu
a.size

# xu ly  toan hoc

a = np.arange(1,1+12, dtype = 'float').reshape(3,4)
b = np.arange(11,11+12, dtype = 'float').reshape(3,4)

g = a + b
c = a/b
d = a *b
#
np.exp(a) # e^a tung phan tu

np.log(np.exp(a)) 

np.sqrt(a) # can bac 2
v = np.array([30,45,60,90])
np.sin(v)
np.cos(a)

b2 = np.array([1,2,2,2,3,4,5,5,6,7,8,9,9])
np.unique(b2) # loai cac bien lap lai

boolar = np.in1d(b2, [2,5]) # 2 , 5 => True , con lai False
    
#------- so sanh cac mang

a == b
a < 2

a.sum()
a.min()
a.min(axis = 0)

a.mean()    # trung binh
np.median(a) # trung vi


h = a.view() # 2 bien cung 1 vung nho, thay doi 1 cai, ca 2 thay doi
a[0,0] = 4
h[0,0] = 1

# tinh toan tren ma tran -----

a.T # dao hang thanh cot
b
c = b.ravel() # chuyen thanh mang 1 chieu

a.resize((2,6)) # chyen thanh 2 hang, 6 cot


np.insert(a,1,5)


df = pd.read_csv('EURUSD_H1.csv' , delimiter = ',')

df['macd']=df['CLOSE'].ewm(span = 12, adjust = False).mean() -df['CLOSE'].ewm(span = 26, adjust = False).mean() 
df['macdplot'] = df['macd'] - df['macd'].ewm(span = 9, adjust = False).mean()
df['rangeCand'] = df['HIGH'] - df['LOW']

def add_col(df,t,colname):
    x = []
    for i in range(len(df)):
        try:
            x.append(df[colname][i-t] / df[colname][i])
        except:
            x.append(0)
    return x


for t in range(1,21):
    df['macdp_'+str(t)] = add_col(df,t,'macdplot')
for t in range(1,21):
    df['rangeCand_'+str(t)] = add_col(df,t,'rangeCand')


result = []
end = False
for i in range(len(df)):
    
    tang = df['CLOSE'][i] * 1.005
    giam = df['CLOSE'][i] * 0.995
    if end :
        break
    for j in range(10):
        if i+j == len(df):
            end = True
           # print(i+j, "end")
            break
        if df['HIGH'][i+j] >= tang:
            result.append(1)
           # print(i+j)
            break
        if df['LOW'][i+j] <= giam:
            result.append(0)
           #print(i+j)
            break
        if j == 9:
            result.append(np.nan)


data_dftest  = df[:len(result)]
data_dftest['y'] = result
data_dftest = data_dftest [21:]

data_dftest = data_dftest[data_dftest.y.notnull()]



xy= np.asarray(data_dftest[:25000])
x_data = xy[: , 7:-1]
y_data = xy[: , [-1]]





model = Sequential()

model.add(Dense(units = 40, input_dim = 43))
#model.add(Dense(units = 30))
#model.add(Dense(units = 40))
model.add(Dense(units = 20))
#model.add(Dense(units = 25))
model.add(Dense(units = 10))
model.add(Dense(units = 15))
#model.add(Dense(units = 10))
model.add(Dense(units = 5))
model.add(Dense(units = 3))
model.add(Dense(units = 1))
# co them lop

model.compile(loss = 'mse' , optimizer=  'rmsprop')

model.summary()

model.fit(x_data,y_data,epochs = 20)



model.predict(np.array([np.asarray(xy[: , 7:-1][1])]))


