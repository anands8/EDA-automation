import dtale
import pandas as pd
df = pd.read_csv("Travel.csv")
d = dtale.show(df)
d.open_browser()