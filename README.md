# cat-detector
Handheld cat detection machine using tensorflow for the classification, and arduino for the implementation.

### Tensorflow Component

This project uses a virtual environment ([venv](https://docs.python.org/3/library/venv.html)) for it's python portion, which allows for
easy installation of required libraries.

If you wish to train the model using your GPU instead of your CPU, you will need to make slight modifications to the repo, but the steps
necessary for this are well documented and are unncessary for me to explain.

```
cd tfmodel
python3 -m venv venv
. venv/bin/activate
pip install requirements.txt
```

To train the dataset, the CIFAR-10 dataset will be used, as there exists a cat label, along with many other objects. If the model returns cat,
that can be read as true.

### Arduino Component

Parts:

Schematic:
