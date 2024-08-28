import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Karachi',
    'appid': 'bcaabf0aaa6d639d22189ecbf43816f4',
    'units': 'metric'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}:")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print(f"Failed to retrieve data: {response.status_code}")
