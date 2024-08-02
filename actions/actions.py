# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests, json

class TellWeather(Action):
    
    def name(self):
        return "action_tell_weather"

    def run(self, dispatcher, tracker, domain):
        

        city=tracker.get_slot('city')
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = city
        API_KEY = 'f2e77720afaafac1fbf25419fee26c37'
        # upadting the URL
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:

           # getting data in the json format
            data = response.json()
           # getting the main dict block
            main = data['main']
           # getting temperature
            temperature = main['temp']
           # getting the humidity
            temperature = temperature - 273.15

            temperature=round(temperature,2)
            humidity = main['humidity']
           # getting the pressure
            pressure = main['pressure']
           # weather report
            report = data['weather']
            weather=report[0]['description']
            dispatcher.utter_message(f'The weather in {CITY} is {weather}')
            dispatcher.utter_message(f'The temperature is {temperature} Celcius')
            
        else:

            dispatcher.utter_message(f'please provide valid city name.') 
        return []
        

