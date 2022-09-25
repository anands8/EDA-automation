#Install the below libaries before importing
import pandas as pd
from pandas_profiling import ProfileReport

profile = ProfileReport(pd.read_csv('Travel.csv'), explorative=True)

profile.to_file("pandasprofiloutput.html")