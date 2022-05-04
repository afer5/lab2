import requests
s_city = "Kyiv,UA"
appid = "ae346281ce2aaf7ed4a07d400cd8f805"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Current visibility:", data['visibility'])
print("Wind speed: ", data['wind']['speed'])
print("------------------------------------")
