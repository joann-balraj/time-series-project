######### Wrangle File for Time Series Project #########

"""
 All functions used in workbook will be put into functions here in order to kerep final report clean and simple 
                                                                                                            """



######### Imports #########

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

import statsmodels.api as sm
from statsmodels.tsa.api import Holt



##### Acquire Function #####

def get_data():
    '''Read data obtained from .csv file on kaggle:'''
    df = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    df = df.dropna()
    df = df[df.City == 'Mexico']
    return df

# Prep Data Function:

def prep_data(df):
    '''
    Converts df to datetime and sorts values and groups by average temperature'''
    return df.assign(ds = pd.to_datetime(df.dt)).sort_values('ds').\
            groupby(['ds'])[['AverageTemperature']].sum()
