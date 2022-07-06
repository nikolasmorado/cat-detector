# cat-detector
Handheld cat detection machine using tensorflow for the classification, and arduino for the implementation.

### Tensorflow Component

This project uses a virtual environment ([venv](https://docs.python.org/3/library/venv.html)) for it's python portion, which allows for easy installation of required libraries.

If you wish to train the model using your GPU instead of your CPU, you will need to make slight modifications to the repo, but the [steps necessary for this are well documented](https://www.tensorflow.org/install/pip#3_gpu_setup) and are unncessary for me to explain.

```
cd tfmodel
python3 -m venv venv
. venv/bin/activate
pip install requirements.txt
```

To train the dataset, the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset will be used, as there exists a cat label, along with many other objects. If the model returns cat, that can be read as true.

I have added my own saved model and .tflite model to the gitignore, as you should train and generate your own, to do such first it is required to run model.py, it will create and train the model, then save it to tfmodel/exported_model. After you have the exported_model directory, run convert.py to generate the .tflite model which will be used on the microcontroller.

```
cd tfmodel
. venv/bin/activate
python model.py
python convert.py
```

You can use the pred.py file make predictions of your own, however you will need to modify the image in the function, it can be run without having generated the .tflite model, but it is necessary for you to have already made, trained, and saved the keras model.


### Arduino Component

Parts:

Schematic:
