# https://ocr.space/OCRAPI
# K87273881388957
# https://api.ocr.space/parse/imageurl?apikey=helloworld&url=
# https://api.ocr.space/parse/imageurl?apikey=helloworld&url=&language=&isOverlayRequired=true
# https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg
# https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/6RJI/image/4NTrD_apkbIr6fIaOxVgM6dlRHM.JPG

import requests
url = 'https://api.ocr.space/parse/imageurl?apikey=K87273881388957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url)
response.raise_for_status()

result = response.json()
# print(type(result))
print(result['ParsedResults'][0]['ParsedText'])