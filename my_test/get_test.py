import requests

url = "http://127.0.0.1:5000/yunos/smart_rate/buy_film_cert"

querystring = {"sql_type":"select","token":"eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ5MjE0MDY0MiwiZXhwIjoxNDkyMjAwNjQyfQ.eyJpZCI6Mn0.cRcT3L-3gF3fyZOCvXwwKj8GDv2iIbE3iIykCrlDt-I","film_id":"12"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "06b83935-9d97-e13a-8547-c2713a9f223d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
