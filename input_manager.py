import pandas as pd
import os
import difflib
import phonenumbers

print("input validation code here!")
df = pd.read_csv("datasets/icd_11.csv")
print(df.head())
