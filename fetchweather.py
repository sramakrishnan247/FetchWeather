import requests
from pprint import pprint


responseip=requests.get('http://ipinfo.io/')
responseip=responseip.json()
city = responseip['city']

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={your api key}")
response=response.json()
print("City: "+str(city))
#print("Weather conditions:"+str(response['weather']['description']))

print("Temperature: "+str(response['main']['temp']-273)+"C")
print("Humidity: "+str(response['main']['humidity']))
