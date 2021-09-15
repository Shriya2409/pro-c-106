import numpy as np
import csv

def getDataSource(path):
    marks=[]
    days_present=[]
    with open(path)as f:
        reader = csv.DictReader(f)
        for row in reader:
           marks.append(float(row["Size of TV"]))
           days_present.append(float(row["Average time spent watching TV in a week"]))
    return{"x":marks, "y":days_present}    

def findCorrelatin(data_source):
    correlation=np.corrcoef(data_source['x'], data_source['y'])
    print("co relation is ", correlation[0,1])

def setup():
    data_path="./data.csv"
    data_source=getDataSource(data_path)
    findCorrelatin(data_source)

setup()