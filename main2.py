import requests

s_city = "Kyiv,UA"
appid = "ae346281ce2aaf7ed4a07d400cd8f805"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\n"
    "Wind speed: ",(i['wind']['speed']), " \r\n"
    "Current visibility :", i['visibility'])
    print("____________________________")
