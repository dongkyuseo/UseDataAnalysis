def yolo5(img):
    import torch

    # 모델
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    
    # 추론
    results = model(img)

    # 결과
    # results.print()
    # results.show()
    # results.save() 
    # Save image to 'runs\detect\exp'

    results.xyxy[0]  # 예측 (tensor)
    result = results.pandas().xyxy[0]  # 예측 (pandas)

    return result['name']