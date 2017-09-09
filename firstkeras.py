from keras.layers import Dense
from keras.models import Sequential
from sklearn.datasets import make_classification
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from keras import callbacks

#Creating my datasets
d=make_classification(n_features=20,n_samples=1000)
#Creates a dataset with 100 sample of 4 features each and 2 outputs
X_train,X_test,Y_train,Y_test=train_test_split(d[0],d[1])
#Successfully Created training and testing datasets


#Creating a Neural Network for classification

model=Sequential()
model.add(Dense(6,activation='relu',input_dim=20))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Created the Neural Network Successfully
remote = callbacks.RemoteMonitor(root='http://localhost:9000')
model.fit(X_train,Y_train,epochs=500,callbacks=[remote])
predict=np.round(model.predict(X_test))
print(accuracy_score(predict,Y_test))