# HtD5CWBY6OLPbIzvSFd6
# Hc57W6u6kK

# http://openapi.naver.com/v1/papago/n2mt
import urllib.request
import json

client_id = "HtD5CWBY6OLPbIzvSFd6"
client_secret = "Hc57W6u6kK"
encoding_text = urllib.parse.quote("우리, 오늘은 뭐할까")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])