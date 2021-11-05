import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

df=pd.read_csv("data.csv")
avgRating=df["Avg Rating"].tolist()
fig=ff.create_distplot([avgRating],["Average Rating"],show_hist=False)

fig.show()
