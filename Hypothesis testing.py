import pandas as pd
from scipy import stats
data  = pd.read_excel("E:/Chart in Microsoft Office PowerPoint.xlsx")
data.describe()
data.Age10.describe()
stats.f_oneway(data.Age_10to15,data.Age_15to20,data.Age_20to25)
