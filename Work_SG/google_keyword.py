from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

pytrends = TrendReq(hl = 'ko-kr', tz = 540)
kw = ['연남동', '연희동']

pytrends.build_payload(kw_list=kw, cat=0, timeframe='2020-01-01 2023-01-01', geo='KR')
data = pytrends.interest_over_time()
# data = data.reset_index()

# print(data.head(20))

data.plot()