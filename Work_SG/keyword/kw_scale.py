import json

path = 'D:\data\Gentrification_DA\Work_SG\keyword\score.json'
with open(path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

dict_, scale = {}, {}
for n in range(60):
    t = list(json_data[str(n)].values())[0]

    for i, j in json_data[str(n)].items():
        json_data[str(n)][i] = round(j / t, 4)

        if i not in dict_:
            dict_[i] = json_data[str(n)][i]

dict_ = sorted(dict_.items(), key=lambda x:x[1], reverse=True)

for k in range(len(dict_)):
    if dict_[k][0] not in scale:
        scale[dict_[k][0]] = 0
    scale[dict_[k][0]] = dict_[k][1]

def save_local(data):
    '''
    json 데이터를 로컬에 저장하는 함수
    '''
    import json
    
    path = 'D:\data\Gentrification_DA\Work_SG\keyword\scale.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

save_local(scale)