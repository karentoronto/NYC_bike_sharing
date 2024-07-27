################################################ DIVVY BIKES DASHABOARD #####################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime as dt
from streamlit_keplergl import keplergl_static


########################### Initial settings for the dashboard ##################################################################


st.set_page_config(page_title = 'NYC Citi Bike Sharing Strategy Dashboard', layout='wide')
st.title("NYC Citi Bike Sharing Strategy Dashboard")
st.markdown("The dashboard will help make informed decisions that will circumvent availability issues.")
st.markdown("The high demand for bike sharing in NYC has led to a distribution problem. This dashboard is a descriptive analysis of existing data and presents actionable insighs to the business strategy team to avoid a distribution problem and ensure the company's position as a leader in eco-friendly transportation solutions in the city.")

########################## Import data ###########################################################################################

df = pd.read_csv('df_final.csv', index_col = 0)
top20 = pd.read_csv('top20.csv', index_col = 0)

# # ######################################### DEFINE THE CHARTS #####################################################################

## Bar chart

fig_1 = px.bar(data_frame = top20, 
             x = 'start_station_name', 
             y ='trips', 
             color= 'trips', 
             color_continuous_scale ='ice_r')

fig_1.update_layout({
    'title': {'text': 'Top 20 Bike-Sharing Facilities Operated by Citi Bike', 'font': {'weight': 'bold'}},
    'xaxis': {'title': {'text': 'Start Station Name', 'font': {'weight': 'bold'}}, 'tickfont': {'size': 10}},
    'yaxis': {'title': {'text': 'Number of Trips', 'font': {'weight': 'bold'}}}
})


st.plotly_chart(fig_1, use_container_width=True)


## Line chart 

fig_2= make_subplots(specs=[[{"secondary_y": True}]])


fig_2.add_trace(
    go.Scatter(
        x=df['started_at'],
        y=df['bike_rides_daily'],
        name='Daily bike rides',
         line=dict(color='blue')
    ),
    secondary_y=False
)

# Adding the second trace
fig_2.add_trace(
    go.Scatter(
        x=df['started_at'],
        y=df['average_temp'],
        name='Daily temperature',
        line=dict(color='red')
    ),
    secondary_y=True
)

# Setting titles for the axes
fig_2.update_layout(
    title_text="Daily Bike Rides and Temperature",
    xaxis_title="Date",
    yaxis_title="Bike Rides",
    yaxis2_title="Temperature"
)

st.plotly_chart(fig_2, use_container_width=True)


### Add the map ###

path_to_html = "NYC Bike Sharing Trips Aggregated.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Aggregated Bike Trips in NYC")
st.components.v1.html(html_data,height=1000)
