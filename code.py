import pandas as pd 
import csv 
import plotly.graph_objects as po 

df=pd.read_csv("data.csv")
result=df.groupby("level")["attempt"].mean()
fig = po.Figure(po.Bar(
    x=result,y=['level 1','level 2','level 3','level 4'],orientation='h'
))
fig.show ()