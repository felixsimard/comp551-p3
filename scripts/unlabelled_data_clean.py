import pandas as pd
import pickle
import numpy as np

"""
This script will convert the predictions that are not False made on the unlabelled dataset
to 2 pickle files containing numpy arrays.

Make sure that ./unlabelled.csv contains the aggregated unlabelled dataset labels. (Some will have values
of False - those correspond to the images that the 5 bag models did not agree on - )

We must make sure the indices of the images and labels match.
"""

# Load the unlabelled images
pickle_juice = open("../image_data/images_ul.pkl", "rb")
arr = pickle.load(pickle_juice)
pickle_juice.close()

# Load our labels
df = pd.read_csv("../unlabelled.csv", usecols=["Category"])

# Get indices that are True
indices = df.index[df['Category'] != "False"].tolist()

# Get images from the indices
export_array = np.take(arr, indices, axis=0)

df_export = df.iloc[indices]
# Turn the strings into numpy arrays
df_export['Category'] = df_export['Category'].apply(lambda x: np.array([int(y) for y in list(x)]))

# Data should be in for of numpy array not DataFrame!
new = np.array([])
for i, row in df_export.iterrows():
    new = np.append(new, row.Category)

# Reshape data so that it has len(indices) amount of entries to match image numpy data.
new = new.reshape((len(indices), 36))

# SAVE PICKLES

with open('./unlabelled_labels.pkl','wb') as f:
    pickle.dump(new, f)

with open('./unlabelled_img.pkl','wb') as f:
    pickle.dump(export_array, f)
