def imageinfo(info):
    import exifread
    import numpy as np
    # Open image file for reading (binary mode)
    f = open(info, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    tags_x = tags['GPS GPSLatitude']
    tags_y = tags['GPS GPSLongitude'] 
    tags_date = tags['Image DateTime']

    time = str(tags['Image DateTime'])
    time_2 = time.split(' ')
    day = time_2[0].replace(':', "")
    time = time_2[1]

    x_1 = str(tags['GPS GPSLatitude'])
    x_2 = x_1[1:-1].split(', ')
    x_3 = x_2[2].split('/')
    x_4 = int(x_3[0])/int(x_3[1])

    x_2[0] = int(x_2[0])
    x_2[1] = int(x_2[1])
    x_2[2] = int(x_4)
    x = x_2

    latDeg = x[0]
    latMin = x[1]
    latSec = x[2]
    x = (int(latDeg)+(int(latMin)/60)+(int(latSec)/3600))


    y_1 = str(tags['GPS GPSLongitude'])
    y_2 = y_1[1:-1].split(', ')
    y_3 = y_2[2].split('/')
    y_4 = int(y_3[0])/int(y_3[1])

    y_2[0] = int(y_2[0])
    y_2[1] = int(y_2[1])
    y_2[2] = int(x_4)
    y = y_2

    lonDeg = y[0]
    lonMin = y[1]
    lonSec = y[2]
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
    area5 = response['results'][0]['region']['area4']['name']

    return x, y, area1, area2, area3, area4, area5, day, time