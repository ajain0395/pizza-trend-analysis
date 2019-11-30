#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashish
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

import plotly.graph_objs as go

flag = True

lata = []
longa = []
bus_name = []

radius = 10
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
mapbox_access_token = 'pk.eyJ1IjoiYWphaW4wMzk1IiwiYSI6ImNqeDczMWNkczAwcngzeHAzaDc2aGptaHIifQ.PrZuFAsV8w5ghhUhe8AF3w'

pizza_data = pd.read_csv("./data/Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv")                 

pizza_data.latitude = pizza_data.latitude.astype(float)
pizza_data.longitude = pizza_data.longitude.astype(float)
app.layout = html.Div(children=[
        
        dcc.Markdown('''
# **Interactive Data Analysis**
'''),
        
        dcc.Markdown('''
        ------
        ###### **Restaurants at different locations in USA**
        ------
    '''),
        html.Div([
                 
                dcc.Graph(
        id='pizza_points',
        figure={
         'data' : [
                    go.Scattermapbox(
                            lat=pizza_data.latitude,
                            lon=pizza_data.longitude,
                            mode='markers',
                            marker=go.scattermapbox.Marker(size=9),
                            text="Restaurant Name: " + pizza_data['name'] + "<br>City: " + pizza_data['city'],
                            )],
 'layout':go.Layout(
                        autosize=True,
                        mapbox_style= 'carto-positron',
                        mapbox_center_lon=np.mean(pizza_data.longitude),
                        mapbox_center_lat=np.mean(pizza_data.latitude),
                        margin={"r":10,"t":0,"l":0,"b":0})
        }
    )],style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
dcc.Markdown('''
        ------
        ###### **Heatmap of Demand of Restaurants**
        ------

    '''),
            html.Div([dcc.Graph(
        id='heat_map',
        figure={
                'data':[go.Scattermapbox(
                            lat=pizza_data.latitude,
                            lon=pizza_data.longitude,
                            mode='markers',
                            marker=go.scattermapbox.Marker(size=9,opacity=0.0000001),
                            text="Restaurant Name: " + pizza_data['name'] + "<br>City: " + pizza_data['city'],
                            ),
                        go.Densitymapbox(lat=pizza_data.latitude,
                                         lon=pizza_data.longitude,

                                         hoverinfo="skip",
                                         radius=radius)],
                'layout':go.Layout(
                        title=go.layout.Title(text='Dash Data Visualization'),
                        autosize=True,
                        mapbox_style= 'stamen-terrain',
                        mapbox_center_lon=np.mean(pizza_data.longitude),
                        mapbox_center_lat=np.mean(pizza_data.latitude),
                        margin={"r":0,"t":0,"l":0,"b":0})
                }
        )
        ],style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
dcc.Markdown('''
        **Darker the region indicates higher demand**

    ''')
],style={'width': '100%','height':'100%'})

if __name__ == '__main__':
    app.run_server(debug=True,port=4253)