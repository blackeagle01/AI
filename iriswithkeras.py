from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from keras.utils import to_categorical
import numpy as np
from keras.models import save_model,load_model
#Iris is a classification based dataset of 150 samples of flowers and four features per flower.


#Loading the iris dataset and splitting it into training and testing data

d=load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(d.data,d.target)
Y_train_nn=to_categorical(Y_train,num_classes=3)
Y_test_nn=to_categorical(Y_test,num_classes=3)

#Creating a Neural Network

model=Sequential()
model.add(Dense(6,activation='relu',input_dim=4))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#Create a Support Vector Machine Classifier
clf=SVC(decision_function_shape='ovr')
clf.fit(X_train,Y_train)
#Train the Neural Net
model.fit(X_train,Y_train_nn,epochs=1000)
save_model(model,'mymodel.h5')
#print((X_test[4].T).shape)
#predict=np.round(model.predict((X_test[6].reshape(1,4))))
#print(predict,Y_test_nn[6])