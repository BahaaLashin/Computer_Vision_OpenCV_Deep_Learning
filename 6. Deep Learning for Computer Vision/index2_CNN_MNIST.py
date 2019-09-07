import matplotlib.pyplot as plt 
import numpy as np 
import cv2
from keras.datasets import mnist

(x_train , y_train ) , (x_test,y_test) = mnist.load_data()

from keras.utils.np_utils import to_categorical

y_train = to_categorical(y_train)
y_test  = to_categorical(y_test)

x_train = x_train/255
x_test  = x_test/255

x_train = x_train.reshape((60000, 28, 28,1))
x_test  = x_test.reshape((10000, 28, 28,1))

from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten

model = Sequential()

model.add(Conv2D(filters=32,kernel_size=(4,4),input_shape=(28,28,1)))
model.add(MaxPool2D((4,4)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=10,activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=50,batch_size=20)

y_pred = model.predict_classes(x_test)

from sklearn.metrics import confusion_matrix , classification_report
confusion = confusion_matrix(y_pred,y_test)
print('confustion matrix')
print(confusion)

classification_report = classification_report(y_pred,y_test)
print('classification report')
print(classification_report)