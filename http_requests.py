import requests

url = "https://devapi.qweather.com/v7/weather/now"
params = {"location": "101280601", "key": "d728d7e682074509a4c8b030f3729e99"}#和风天下以location位置ID传入城市
response = requests.get(url, params=params)  # 发送GET请求

if response.status_code == 200:
    data = response.json()  # 解析JSON响应
    print(f"当前温度：{data['now']['temp']}℃")
    print(f"当前天气：{data['now']['text']}")
    print(f"当前风向：{data['now']['windDir']}")
else:
    print(f"请求失败，错误码：{response.status_code}")