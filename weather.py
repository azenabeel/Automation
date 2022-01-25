import requests

API_KEY = "34cd53393b59654fde54248275f6c4af"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ") # anything thats after ? is query parameter
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temprature = round( data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Temprature: ", temprature, "celsius")
else:
    print("An error occured.")
