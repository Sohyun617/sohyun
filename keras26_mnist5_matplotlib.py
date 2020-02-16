from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.callbacks import EarlyStopping
import numpy as np 

(x_train, y_train),(x_test, y_test) = mnist.load_data()

# print(x_train)
# print(y_train)
print(x_train.shape) 
print(y_train.shape)

x_train = x_train.reshape(x_train.shape[0],28*28).astype('float32')/255
x_test = x_test.reshape(x_test.shape[0],28*28).astype('float32')/255

print(x_train.shape)
print(y_train.shape)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(32, input_shape =(28*28,))) 
model.add(Dense(10))
model.add(Dense(10))
model.add(Dense(1)) 

model.summary()

model.compile(loss='mse',
              optimizer='adam',
              metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='loss', patience=20)

hist = model.fit(x_train,y_train, validation_split=0.2,
                epochs=50, batch_size=8, verbose=1, 
                callbacks=[early_stopping])
model.evaluate(x_test, y_test)
print(hist.history.keys())

import matplotlib.pyplot as plt

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model loss, accuracy')
plt.ylabel('loss, acc')
plt.xlabel('epoch')
plt.legend(['train loss', 'test loss', 'train acc','test acc'])
plt.show()


# acc=model.evaluate(x_test, y_test)
# print(acc)
