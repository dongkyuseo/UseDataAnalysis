def face(image_path):
        
    # key 암호화
    filename= 'keys/facekey.txt'

    with open(filename) as f:
        api_key = f.read()
    
    import os
    import sys
    import requests
    import json
    client_id = api_key.split('\n')[0]
    client_secret = api_key.split('\n')[1]
    url = "https://naveropenapi.apigw.ntruss.com/vision/v1/face"
    files = {'image': open(image_path, 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    tmp = response.json()
    img_gender = tmp['faces'][0]['gender']['value']
    img_age = tmp['faces'][0]['age']['value']
    img_emo = tmp['faces'][0]['emotion']['value']
    img_pose = tmp['faces'][0]['pose']['value']
    return img_gender, img_age, img_emo, img_pose