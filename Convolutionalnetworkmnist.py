from keras.datasets import mnist
from keras.models import Sequential
from keras.layers  import Dense,Dropout,Conv2D,MaxPooling2D,Flatten
from keras.utils import to_categorical
#Split the datasets into training and testing modules

(X_train,Y_train),(X_test,Y_test)=mnist.load_data()
X_train.resize(60000,28,28,1)
X_test.resize(len(X_test),28,28,1)
Y_train=to_categorical(Y_train,num_classes=10)
Y_test=to_categorical(Y_test,num_classes=10)
#Create a Convolutional Neural Network

model=Sequential()
model.add(Conv2D(filters=20,kernel_size=(3,3),padding='same',activation='relu',input_shape=X_train.shape[1:]))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.4))
#model.add(Conv2D(filters=32,kernel_size=(3,3),padding='same',activation='relu'))
#model.add(MaxPooling2D(pool_size=(2,2)))

## Create the last Dense block

model.add(Flatten())
model.add(Dense(80,activation='relu'))
#model.add(Dense(80,activation='relu'))
model.add(Dropout(0.4))
#model.add(Dense(80,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

##Start training

model.fit(X_train,Y_train,epochs=100)
model.save('conv_model.h5')