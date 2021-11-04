def weather(day, area1):
    import pandas as pd
    import os
    from datetime import datetime, timedelta
    import urllib.request
    import json
    from pandas import Series
    import requests

    # key 암호화
    filename= 'keys/weather.txt'

    # KEY 로드
    with open(filename) as f:
        api_key = f.read()
    
    ac = pd.read_csv('data/areacode.csv')

    # 날짜 지정
    startDt = day
    si = area1
    # 지역 코드 선택

    for i in range(len(ac['지점명'])):
        sa = Series(si)
        if sa.str.contains(ac['지점명'][i])[0] == True:
            area = ac['지점'][i]

    stnIds = area
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    params ={'serviceKey' : api_key, 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'json', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : startDt, 'endDt' : startDt, 'stnIds' : stnIds }

    response = requests.get(url, params=params).json()
    df = pd.DataFrame(response['response']['body']['items']['item'])
   # 평균상대습도, 평균지면온도, 일 강수량, 일 최심적설
    return df[['avgRhm', 'avgTs', 'sumRn', 'ddMes']]