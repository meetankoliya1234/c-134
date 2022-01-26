import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

df = []

with open("Star_with_gravity.csv", "r") as m:
    csvreader = csv.reader(m)
    for dt in csvreader:
        df.append(dt)

print(df[0])