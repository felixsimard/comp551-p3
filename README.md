# comp551-p3
Mini-Project 3 for COMP551 Applied Machine Learning @ McGill University Fall 2021. Objective of this assignment is to classify an image containing one upper- or lower-case character (A-Z, a-z) and one number (0-9). The image classifier will be trained/validated/tested on 30K labelled image instances and 30K unlabelled instances.

## Dataset

- `images_l.pkl` - Image data, 30K samples (56x56 px)
- `labels_l.pkl` - Labels for image data (36 bit vector)
- `images_ul.pkl` - Unlabelled additional images
- `images_test.pkl` - Dataset to test image classifier on
- To open a `.pkl` file:
```py
import pickle
f = open("PATH", 'rb')
data = pickle.load(f)
```   
