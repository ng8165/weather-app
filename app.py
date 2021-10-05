import requests
from PyQt6.QtWidgets import QApplication, QWidget

location = input("Enter location: ")

geo = requests.get("https://geocode.xyz/" + location + "?json=1").json()
points = requests.get("https://api.weather.gov/points/" + geo["latt"] + "," + geo["longt"]).json()
forecast = requests.get(points["properties"]["forecast"]).json()

# print("Weather for " + points["properties"]["relativeLocation"]["properties"]["city"] + ", ", end="")
# print(points["properties"]["relativeLocation"]["properties"]["state"] + ":\n")

for i in range(14):
    day = forecast["properties"]["periods"][i]
    print(day["name"] + ": ", end="")
    print(str(day["temperature"]) + "°" + day["temperatureUnit"] + ", ", end="")
    print(day["shortForecast"])
