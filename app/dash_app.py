"""Dash app: success pie chart and payload/outcome scatter."""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash,dcc,html,Input,Output
DATA=Path(__file__).resolve().parents[1]/"data"/"spacex_launch_dash.csv"
if not DATA.exists(): raise FileNotFoundError("Place dashboard data at data/spacex_launch_dash.csv")
df=pd.read_csv(DATA)
app=Dash(__name__)
app.layout=html.Div([html.H1("SpaceX Launch Analytics"),dcc.Dropdown(["All"]+sorted(df.LaunchSite.dropna().unique()),"All",id="site"),dcc.Graph(id="pie"),dcc.Graph(id="scatter")])
@app.callback(Output("pie","figure"),Output("scatter","figure"),Input("site","value"))
def update(site):
 d=df if site=="All" else df[df.LaunchSite==site]
 return (px.pie(d,names="Class",title="Landing outcome distribution"),
         px.scatter(d,x="PayloadMass",y="Class",color="Class",title="Payload mass vs landing outcome"))
if __name__=="__main__": app.run(debug=False)
