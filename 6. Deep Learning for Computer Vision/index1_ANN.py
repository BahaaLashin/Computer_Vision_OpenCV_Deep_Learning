import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_csv('Churn_Modelling.csv')

X = data.iloc[:,3:13].values
y = data.iloc[:,13].values

from sklearn.preprocessing import OneHotEncoder,LabelEncoder

lb1 = LabelEncoder()
X[:,1] = lb1.fit_transform(X[:,1])

lb2 = LabelEncoder()
X[:,2] = lb2.fit_transform(X[:,2])

oneHot = OneHotEncoder(categorical_features=[1])
X = oneHot.fit_transform(X).toarray()

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(X,y,test_size=.2,random_state=42)

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
x_train = scale.fit_transform(x_train)
x_test = scale.transform(x_test)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(input_dim=12,units=6,activation='relu'))
model.add(Dense(units=6,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=100,batch_size=20)

pred_y = model.predict_classes(x_test)

from sklearn.metrics import confusion_matrix,classification_report

classification_report = classification_report(pred_y,y_test)
print('classification report')
print(classification_report)

confusion_matrix = confusion_matrix(y_test,pred_y)
print('Confusion Matrix')
print(confusion_matrix)
