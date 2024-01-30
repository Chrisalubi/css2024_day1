# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:51:41 2024

@author: User
"""

import pandas as pd

file = pd.read_csv("iris.csv")

file = pd.read_csv("data_02/iris.csv")

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

file = pd.read_csv(url, header=None, names = column_names)

df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

file = pd.read_excel("residentdoctors.xlsx")

print(file)

file = pd.read_json("data_02/student_data.json")

print(file)