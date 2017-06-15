# Training and running a linear model using Scikit-Learn

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# load the data
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")

# prepare the data
country_stats = pre