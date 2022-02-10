import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks=[]
    dayspresent=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Days Present"]))
            dayspresent.append(float(row["Marks In Percentage"]))
    
    return{"x":marks,"y":dayspresent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Marks vs number od days present: ",correlation[0,1])

def setup():
    data_path="StudentMarks.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()