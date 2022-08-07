import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([Dense(units=1, input_shape=[1])]) #define the layer and its neurons. In this case 1 layer with 1 neuron
model.compile(optimizer='sgd', loss='mean_squared_error') #here is where the heavy calculus ops are execution behind the scenes. Abstract to us

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float) # x= -1, 0, 1, 2, 3, 4
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float) # y= -3, -1, 1, 3, 5, 7

model.fit(xs, ys, epochs=500) # This is the neural network learning process

print(model.predict([10, 0])) # Asking the model to predict what will be the value of Y when X is 10

# Output [[18.97963  ][-0.9908468]]
