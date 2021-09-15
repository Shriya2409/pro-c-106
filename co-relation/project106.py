import numpy as np
import csv
import plotly_express as px

def getDataSource(path):
    marks=[]
    days_present=[]
    with open(path)as f:
        reader = csv.DictReader(f)
        fig=px.scatter(reader, x="Marks In Percentage", y="Days Present")
        fig.show()
        for row in reader:
           marks.append(float(row["Marks In Percentage"]))
           days_present.append(float(row["Days Present"]))
    return{"x":marks, "y":days_present}    

def findCorrelatin(data_source):
    correlation=np.corrcoef(data_source['x'], data_source['y'])
    print("co relation is ", correlation[0,1])

def setup():
    data_path="./data2.csv"
    data_source=getDataSource(data_path)
    findCorrelatin(data_source)

setup()