import numpy as np 
import matplotlib.pyplot as plt 
import cv2

from keras.preprocessing.image import ImageDataGenerator

image_gen = ImageDataGenerator(
    rotation_range=30,
    height_shift_range=.2,
    width_shift_range=.2,
    rescale= 1/255,
    shear_range=0.2,
    zoom_range=0.3,
    horizontal_flip=True
)
# data = image_gen.flow_from_directory('dataset/training_set')

from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Dropout,Flatten

input_targert = (150,150,3)

model = Sequential()

model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=input_targert,activation='relu'))
model.add(MaxPool2D(pool_size= (2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),input_shape=input_targert,activation='relu'))
model.add(MaxPool2D(pool_size= (2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),input_shape=input_targert,activation='relu'))
model.add(MaxPool2D(pool_size= (2,2)))


model.add(Flatten())

model.add(Dense(units=128,activation='relu'))
model.add(Dropout(.5))

model.add(Dense(units=1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

training_data = image_gen.flow_from_directory('dataset/training_set',target_size=input_targert[:2],batch_size=16,class_mode='binary')

test_data = image_gen.flow_from_directory('dataset/test_set',target_size=input_targert[:2],batch_size=16,class_mode='binary')

result = model.fit_generator(training_data,epochs=10,steps_per_epoch=150,validation_data = test_data,validation_steps=12)

plt.plot(result.history['acc'])
plt.show()
