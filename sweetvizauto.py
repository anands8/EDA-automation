import pandas as pd
import sweetviz as sv

sweet_report = sv.analyze(pd.read_csv("Travel.csv"))

sweet_report.show_html('sweet_report.html')