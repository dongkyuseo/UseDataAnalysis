def imageinfo(info):
    from PIL import Image
    from PIL.ExifTags import TAGS
    taglabel = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value

    latDeg = taglabel['GPSInfo'][2][0]
    latMin = taglabel['GPSInfo'][2][1]
    latSec = taglabel['GPSInfo'][2][2]

    import numpy as np
    x = (int(latDeg)+(int(latMin)/60)+(int(latSec)/3600))
    
    lonDeg = taglabel['GPSInfo'][4][0]
    lonMin = taglabel['GPSInfo'][4][1]
    lonSec = taglabel['GPSInfo'][4][2]


    y = int(lonDeg)+(int(lonMin)/60)+(int(lonSec)/3600)

    # key 암호화
    filename= 'keys/mapkey.txt'

    with open(filename) as f:
        api_key = f.read()
    
    client_id = api_key.split('\n')[0]
    client_secret = api_key.split('\n')[1]

    import requests

    url = f"https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords={y},{x}&sourcecrs=epsg:4326&orders=legalcode&output=json&orders=addr,admcode,roadaddr"

    payload={}
    headers = {
    'X-NCP-APIGW-API-KEY-ID': client_id,
    'X-NCP-APIGW-API-KEY': client_secret
    }

    response = requests.get(url, headers=headers, data=payload).json()
    
    area1 = response['results'][0]['region']['area1']['alias']
    area2 = response['results'][0]['region']['area1']['name']
    area3 = response['results'][0]['region']['area2']['name']
    area4 = response['results'][0]['region']['area3']['name']
    day = taglabel['DateTime'][:10]
    day = day.replace(':', "")
    time = taglabel['DateTime'][11:]

    return x, y, area1, area2, area3, area4, day, time