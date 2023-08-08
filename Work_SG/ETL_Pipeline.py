def extract():
    '''
    api 데이터 호출 함수
    '''
    import os
    import requests
    import xmltodict
    from dotenv import load_dotenv
    load_dotenv()

    service_key = os.environ.get('servicekey')
    url = 'http://apis.data.go.kr/1611000/nsdi/IndvdLandPriceService/attr/getIndvdLandPriceAttr'
    params ={'serviceKey' : service_key, 'pnu' : '1111017700102110000', 'stdrYear' : '2015', 'format' : 'xml', 'numOfRows' : '10', 'pageNo' : '1' }

    response = requests.get(url, params=params)
    html = response.text
    html_dict = xmltodict.parse(html)
    return html_dict

def transform():
    '''
    데이터 변환 함수
    '''
    pass

def s3_connection():
    '''
    aws S3에 연결하는 함수
    '''
    import os
    import boto3
    from dotenv import load_dotenv
    load_dotenv()

    aws_access_key_id = os.environ.get('aws_access_key_id')
    aws_secret_access_key = os.environ.get('aws_secret_access_key')

    try:
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!") 
        return s3

def load():
    '''
    AWS S3에 적재하는 함수
    '''
    pass

def save_local(data):
    '''
    json 데이터를 로컬에 저장하는 함수
    '''
    import json
    
    path = 'D:/data/project/test1.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

file = extract()
# print(file)

save_local(file)