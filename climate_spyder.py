# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:56:35 2021

@author: alindqu1
"""
import pandas as pd

#import .csv file as a pandas dataframe
all_data = pd.read_csv(r'C:\Users\alindqu1\iCloudDrive\Data_Analytics\proj1_climatechange\results.csv')

#make the year column the index for the dataframe
all_data.set_index(all_data['year'], inplace=True)

#separate world and minneapolis data
mpls = all_data[["mpls_temp"]]
world = all_data[["global_temp"]]

#calculate Minneapolis moving average
mav_mpls = mpls.rolling(window=7).mean()

#calculate global moving average
mav_world = world.rolling(window=7).mean()

#create the plots
mav_mpls['mpls_temp'].plot(ylabel='Average Temp (C)', xlabel='Year', title='Global and Local Average Annual Temperatures', legend=True, grid=True)
mav_world['global_temp'].plot(legend=True, grid=True, xlabel='Year')
