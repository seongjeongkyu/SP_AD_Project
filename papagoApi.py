import requests
import urllib.request

def papago(text, outputKey):
    detectUrl = "https://openapi.naver.com/v1/papago/detectLangs"
    client_id = "752mMukTdRRPCMcsy6D1"          #언어감지 ID
    client_secret = "uIay38uRaR"                #언어감지 password
    request_url = "https://openapi.naver.com/v1/papago/n2mt"
    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    request = urllib.request.Request(detectUrl)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        a = response_body.decode('utf-8').split(":")
        key = a[1][:-1]
        key = key.replace('"',"")
        # print(key)
    else:
        print("Error Code:" + rescode)
    inputKey = key
    headers = {"X-Naver-Client-Id": "80UYvzV6PMF68t_NAnlD", "X-Naver-Client-Secret": "6usybgQiul"}
    # print(outputKey)
    params = {"source": inputKey, "target": outputKey, "text": text}
    response = requests.post(request_url, headers=headers, data=params)

    result = response.json()
    transResult = result['message']['result']['translatedText']
    return transResult
