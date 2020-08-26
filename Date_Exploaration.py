import os
from os import listdir
import pandas as pd
import numpy as np
import glob
import tqdm
from typing import Dict
import matplotlib.pyplot as plt

#plotly
#!pip install chart_studio
import plotly.express as px
#import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot
import cufflinks
cufflinks.go_offline()
cufflinks.set_config_file(world_readable=True, theme='pearl')

#color
from colorama import Fore, Back, Style

import seaborn as sns
sns.set(style="whitegrid")

#pydicom
import pydicom

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Settings for pretty nice plots
plt.style.use('fivethirtyeight')
plt.show()


# file reading
#print(list(os.listdir("osic-pulmonary-fibrosis-progression")))

train_df = pd.read_csv('osic-pulmonary-fibrosis-progression/train.csv')
test_df = pd.read_csv('osic-pulmonary-fibrosis-progression/test.csv')

#print('Training data shape: ',Style.RESET_ALL,train_df.shape)
#print(train_df.head(5))

#basic info
print(Fore.YELLOW + 'Train Set !!',Style.RESET_ALL)
print(train_df.info())
print('-------------')
print(Fore.BLUE + 'Test Set !!',Style.RESET_ALL)
print(test_df.info())