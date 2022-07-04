import tensorflow as tf
from tensorflow import keras
import numpy as np

(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0


def create_model():
    model = keras.models.Sequential([
        keras.layers.Conv2D(
            32,
            (3, 3),
            activation = 'relu',
            input_shape = (32, 32, 3)
        ),

        keras.layers.MaxPooling2D(
            (2, 2)
        ),

        keras.layers.Conv2D(
            64,
            (3, 3),
            activation = 'relu',
        ),

        keras.layers.MaxPooling2D(
            (2, 2)
        ),

        keras.layers.Conv2D(
            64,
            (3, 3),
            activation = 'relu',
        ),

        keras.layers.Flatten(),

        keras.layers.Dense(
            64,
            activation = 'relu',
        ),

        keras.layers.Dense(
            10,
        )
    ])

    model.compile(
        optimizer = 'adam',
        loss = keras.losses.SparseCategoricalCrossentropy(from_logits = True),
        metrics = ['accuracy']
    )
    
    return model

model = create_model()

model.fit(
    train_images,
    train_labels,
    epochs = 10,
    validation_data = (test_images, test_labels)
)

model.save('exported_model')