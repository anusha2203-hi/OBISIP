#WEATHER_APP
import requests
api_key='62b79cd924f8dc657c16d2764318f5b6'
user_input=input("Enter city: ")
print(user_input)
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod']=='404':
    print("No city found")
else:
    weather=weather_data.json()['weather'][0]['main']
    temp=round((weather_data.json()['main']['temp']-32)*(5/9))
print(f"Weather in {user_input} is: {weather}")
print(f"Temperature in {user_input} is: {temp}°C")