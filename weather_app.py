import requests
import json 
import pyttsx3

engine = pyttsx3.init()
city = input("Enter the name of city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=398a3054ecbe4e98909124915250708&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()


