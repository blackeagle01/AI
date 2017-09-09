from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense,Dropout
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification
from keras.utils import to_categorical
import numpy as np
from keras.models import load_model


def accuracy_score(y1,y2):
	total=len(y1)
	count=0
	for i,j in zip(y1,y2):
		if np.all(i==j):
			count+=1
	return count/total

## data loading and preprocessing

d=load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(d.data,d.target)
Y_train=to_categorical(Y_train,num_classes=3)
Y_test=to_categorical(Y_test,num_classes=3)

## model building
'''
model=Sequential()
model.add(Dense(6,activation='relu',input_dim=4))
model.add(Dense(6,activation='relu'))
model.add(Dropout(0.3))
#model.add(Dense(6,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

## Model training and saving the model
model.fit(X_train,Y_train,epochs=1000)
model.save('mymodel.h5')

'''
model=load_model('mymodel.h5')
#print(np.round(model.predict(X_test)))

#print('____________________________________')
#print('\n')

#print(Y_test)
predict=np.round(model.predict(X_test[:8]))
print(predict,'\n',Y_test[:8])