import requests
from pprint import pprint


responseip=requests.get('http://ipinfo.io/')
responseip=responseip.json()
city = responseip['city']

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e81aa24b21cefcb8f32a709177a63342")
response=response.json()
print("City: "+str(city))
#print("Weather conditions:"+str(response['weather']['description']))

print("Temperature: "+str(response['main']['temp']-273)+"C")
print("Humidity: "+str(response['main']['humidity']))