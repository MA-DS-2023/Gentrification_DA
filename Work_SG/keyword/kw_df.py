from pytrends.request import TrendReq
import pandas as pd
import json
import time

path = 'D:\data\Gentrification_DA\Work_SG\keyword\scale.json'
with open(path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

kw = []
for i, j in json_data.items():
    kw.append(i)

kw_ = kw[1:]

pytrends = TrendReq(hl = 'ko-kr', tz = 540)

pytrends.build_payload(kw_list=['이태원']+kw_[0:4], cat=0, timeframe='2004-01-01 2023-01-01', geo='KR')
data = pytrends.interest_over_time()
data = data.reset_index()

df = pd.DataFrame(data)
df = df.drop('isPartial', axis=1)
df.to_csv('D:\data\Gentrification_DA\Work_SG\keyword\data/1.csv', encoding='utf-8')

for i in range(4, len(kw_), 4):
    if len(kw_) - i < 4:
        pytrends.build_payload(kw_list=['이태원']+kw_[i:-1], cat=0, timeframe='2004-01-01 2023-01-01', geo='KR')
        data = pytrends.interest_over_time()
        data = data.reset_index()

        df1 = pd.DataFrame(data)
        df1 = df1.drop(['date','isPartial','이태원'], axis=1)
        df1.to_csv(f'D:\data\Gentrification_DA\Work_SG\keyword\data\{int(i/4)+1}.csv')
    else:
        pytrends.build_payload(kw_list=['이태원']+kw_[i:i+4], cat=0, timeframe='2004-01-01 2023-01-01', geo='KR')
        data = pytrends.interest_over_time()
        data = data.reset_index()

        df1 = pd.DataFrame(data)
        df1 = df1.drop(['date','isPartial','이태원'], axis=1)
        df1.to_csv(f'D:\data\Gentrification_DA\Work_SG\keyword\data\{int(i/4)+1}.csv')
        
    time.sleep(10)

df = pd.read_csv('D:\data\Gentrification_DA\Work_SG\keyword\data\kw_data.csv', encoding='utf-8', index_col=0)

for j in range(2,60):
    df1 = pd.read_csv(f'./data/{j}.csv', encoding='utf-8', index_col=0)
    df = pd.concat([df, df1], axis=1)

df.to_csv('D:\data\Gentrification_DA\Work_SG\keyword\kw_data.csv', encoding='utf-8')