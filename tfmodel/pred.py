import tensorflow as tf
import numpy as np

def load_img(fname):
    image = tf.keras.preprocessing.image.load_img(
        fname,
        target_size = (32, 32)
    )
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    return input_arr

model = tf.keras.models.load_model('exported_model')

ret = model.predict(load_img('olivia.png'))

labels = np.array([
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck'])

cmax = 0.0
cclass = 0
for n in range(10):
    if cmax < ret[0][n]:
        cmax = ret[0][n]
        cclass = n
    print(cmax)

print("=========================")
print(ret)
print(labels[cclass])