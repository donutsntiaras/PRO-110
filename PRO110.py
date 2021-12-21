import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

mean=statistics.mean(data)
print("population mean: ", mean)

def dataSet():
    dataset=[]
    for i in range(0,30):
        ran=random.randint(0,len(data))
        v=data[ran]
        dataset.append(v)
    mean2=statistics.mean(dataset)
    return(mean2)

def  graph(mSet):
    graph=ff.create_distplot([mSet], ["reading time"], show_hist=False)
    graph.show()

def setup():
    mSet = []
    for i in range(0,100):
        means=dataSet()
        mSet.append(means)
    graph(mSet)
    mean3=statistics.mean(mSet)
    print("sampling mean: ", mean3)

setup()


