import tensorflow as tf


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.95):
            self.model.stop_training = True
            print(f'\nReached 95% accuracy on epoch {epoch}')

callbacks = myCallback()

data = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = data.load_data()

training_images = training_images / 255.0
test_images = test_images / 255.0

layers = tf.keras.layers
neuralNetwork = tf.nn

# Definition of the neural network
model = tf.keras.models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation=neuralNetwork.relu),
    layers.Dense(10, activation=neuralNetwork.softmax)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=50, callbacks=[callbacks])

# model.evaluate(test_images, test_labels)

#classifications = model.predict(test_images)
#print(classifications[3])
#print(test_labels[3])

