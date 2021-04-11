import csv
import plotly.express as px
import numpy as np
def GetDataSource(datapath):
    Marks = []
    Days = []

    with open (datapath) as csv_files:
        df=csv.DictReader(csv_files)
        for row in df:
            Marks.append(float(row['Marks In Percentage']))
            Days.append(float(row['Days Present']))
    return {'x':Marks, 'y':Days}

       # fig=px.scatter(df,x='Temperature', y='Ice-cream Sales')
        # fig.show()
def FindCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'], datasource['y'])
    print('correlation between marks and days-->',correlation[0,1])

def Setup():
    datapath='Student.csv'
    datasource=GetDataSource(datapath)
    FindCorrelation(datasource)

Setup()