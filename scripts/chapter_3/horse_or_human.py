from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
import tensorflow as tf
from scipy import *
import numpy as np
from keras.preprocessing import image
import os
 
# Prepare training dataset (Rescale all images by 1/255)
train_datagen = ImageDataGenerator(rescale=1/255)
training_directory = 'horse-or-human/training/'
train_generator = train_datagen.flow_from_directory(training_directory, target_size=(300, 300), class_mode='binary')

# Prepare validation dataset (Rescale all images by 1/255)
validation_datagen = ImageDataGenerator(rescale=1/255)
validation_directory = 'horse-or-human/validation/'
validation_generator = validation_datagen.flow_from_directory(validation_directory, target_size=(300, 300), class_mode='binary')

layers = tf.keras.layers

model = tf.keras.models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(loss='binary_crossentropy', optimizer=RMSprop(learning_rate=0.001), metrics=['accuracy'])

history = model.fit(train_generator, epochs=15, validation_data=validation_generator)

# Run prediction after model is trained

#Prepare prediction images and get the model to work

prediction_directory = 'horse-or-human/run_model/'

for filename in os.listdir(prediction_directory):
    img = tf.keras.utils.load_img(prediction_directory + filename, target_size=(300, 300))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    image_tensor = np.vstack([x])
    classes = model.predict(image_tensor)

    print(classes)
    print(classes[0])

    if(classes[0]>0.5): print(filename + 'is a human')
    else: print(filename + 'is a horse')
