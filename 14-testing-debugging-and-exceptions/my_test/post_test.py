import requests

url = "http://127.0.0.1:5000/yunos/smart_rate/buy_film_cert"

querystring = {"sql_type":"insert","token":"eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ5MjA1NTA2NywiZXhwIjoxNDkyMTE1MDY3fQ.eyJpZCI6Mn0.hCtMvQ2cfp7kH_9kbn-nu_4FlDBsRWRg0p4VYCH8ezw","film_id":"710","expire_days":"1","beans_amount":"1"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "2dbb2b6f-cf0a-d8cf-8fee-fb5a2cd1549b"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
