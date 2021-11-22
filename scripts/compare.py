import pandas as pd

"""
This script is simply used to compare output predictions of 2 models.
"""

PATH_TO_CSV_1 = "../BEST_MODELS/final.csv"  # This model gave 90%
PATH_TO_CSV_2 = "../BEST_MODELS/bags.csv"   # This model gave 89%
NEW_CSV = "../bags/felix_l_ul_trained.csv" # new path to test

df = pd.read_csv(PATH_TO_CSV_1)
df2 = pd.read_csv(NEW_CSV)

newDf = pd.DataFrame(df["Category"] == df2["Category"])
newDf = newDf[newDf.Category]

print("Scores are same for: " + str(len(newDf)) + " of the 15000 predictions")
print("Final score can increase by a maximum of: " + str((15000 - len(newDf)) / 15000) + " percent")
