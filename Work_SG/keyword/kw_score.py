from pytrends.request import TrendReq
import pandas as pd
import numpy as np
from numpyencoder import NumpyEncoder
import json

path = 'D:\data\Gentrification_DA\Work_SG\keyword\list.json'
with open(path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

kw = []
for i in list(json_data.keys()):
    for j in list(json_data[i].keys()):
        if j == '삼청동':
            pass
        else:
            kw.append(j)

score = {}
for k in range(60):
    if k == 59:
        kw_ = ['삼청동'] + kw[(k * 4) : -1]
    else:
        kw_ = ['삼청동'] + kw[(k * 4) : (k * 4) + 4]

    pytrends = TrendReq(hl = 'ko-kr', tz = 540)
    pytrends.build_payload(kw_list=kw_, cat=0, timeframe='2004-01-01 2023-01-01', geo='KR')
    data = pytrends.interest_over_time()
    data = data.reset_index()

    df = pd.DataFrame(data)
    df = df.drop('isPartial', axis=1)

    arr = {}

    for i in list(df.columns)[1:]:
        if i not in score:
            arr[i] = 0
        arr[i] = sum(np.array(df[i]))

    score[k] = arr

def save_local(data):
    '''
    json 데이터를 로컬에 저장하는 함수
    '''
    import json
    
    path = 'D:\data\Gentrification_DA\Work_SG\keyword\score.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, cls=NumpyEncoder)

save_local(score)