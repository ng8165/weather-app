import requests

# print("Hello World")

result = requests.get("https://google.com")
# print(result)
print(result.text)
