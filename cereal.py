import os
import csv


#different codes
cereal_csv = os.path.join("..", "LearnPython", "cereal.csv")
with open(cereal_csv) as file: 
    print(file)