import requests

loc = requests.get("https://api.weather.gov/points/37.2980448,-122.0078557")
weather = requests.get(loc.json()["properties"]["forecast"])

print("Weather for " + loc.json()["properties"]["relativeLocation"]["properties"]["city"] + ", ", end="")
print(loc.json()["properties"]["relativeLocation"]["properties"]["state"] + ":\n")
for i in range(14):
    day = weather.json()["properties"]["periods"][i]
    print(day["name"] + ": ", end="")
    print(str(day["temperature"]) + "°" + day["temperatureUnit"] + ", ", end="")
    print(day["shortForecast"])
