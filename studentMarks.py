import plotly.express as px
import csv

with open("StudentMarks.csv") as csv_file:
  df=csv.DictReader(csv_file)
  fig=px.bar(df,x="Days Present",y="Marks In Percentage")
  fig.show()