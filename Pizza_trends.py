#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:30:57 2019

@author: ashish
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.tools as tls
import numpy as np
#import plotly.plotly as py
import plotly.graph_objs as go
#import geopandas as gpd
import os
import time

#import MapParseFinal as map
flag = True
#import threading
lata = []
longa = []
bus_name = []

radius = 10
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
mapbox_access_token = 'pk.eyJ1IjoiYWphaW4wMzk1IiwiYSI6ImNqeDczMWNkczAwcngzeHAzaDc2aGptaHIifQ.PrZuFAsV8w5ghhUhe8AF3w'


#stream_ids = tls.get_credentials_file()['stream_ids']

#stream_id = stream_ids[0]
#df = pd.read_csv(
#    'https://gist.githubusercontent.com/chriddyp/' +
#    '5d1ea79569ed194d432e56108a04d188/raw/' +
#    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#    'gdp-life-exp-2007.csv')
pizza_data = pd.read_csv("./data/Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv")                 
#      stream = stream_bus,

#stream_bus = go.Stream(
#    token=stream_id,  # link stream id to 'token' key
#    maxpoints=500      # keep a max of 80 pts on screen
#)
#livelocation = go.Scattermapbox(
#                            lat=[],
#                            lon=[],
#                            stream = stream_bus,
#                            mode='markers',
#                            marker=go.scattermapbox.Marker(size=9),
#                            text=[])

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
        id='dtc_stops',
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
#            'layout' : go.Layout(
#                autosize=True,
##                height=np.inf,
##                width = np.inf,
#                hovermode='closest',
#                mapbox=go.layout.Mapbox(
#                    accesstoken=mapbox_access_token,
#                    bearing=0,
#                    center=go.layout.mapbox.Center(
#                        lat=np.mean(pizza_data.latitude),
#                        lon=np.mean(pizza_data.longitude)
#                    ),
#                    pitch=2,
#                    zoom=2
#                ),)
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
#                                         z=pizza_data['postalCode'],
#                                         text=pizza_data['name'],
#                                         hovertext=pizza_data['name'],
                                         hoverinfo="skip",
                                         radius=radius)],
#        'data':[go.Densitymapbox(pizza_data,lat='latitude', lon='longitude',hovertext='name', radius=radius)],
#                open-street-map, white-bg, carto-positron, carto-darkmatter, stamen-terrain, stamen-toner, stamen-watercolor
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
#    fig = go.Figure(go.Densitymapbox(lat=pizza_data.latitude, lon=pizza_data.longitude, radius=radius))
#    fig.update_layout(mapbox_style="dark")
#    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#    fig.show()
    app.run_server(debug=True,port=4253)