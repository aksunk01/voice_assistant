import requests
import openai
import base64
import os
import google.generativeai as genai

#Need to validate the app name somehow
def weather(prompt):
    key = #enter your own google gemini key
    genai.configure(api_key= key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    ai_prompt = "What is the city being said, and only give me the city name:",prompt
    response = model.generate_content(ai_prompt)
    message = str(response.text)
    
    
 
    #print(len((response.text)))

    api = f"http://api.weatherapi.com/v1/current.json?key=072cad3a8f1d4fb2bfb185306232409&q={response.text.strip()}&aqi=no"
    data = requests.get(api).json()
    return(f"The temperature is {data['current']['temp_f']} F, The humidity is {data['current']['humidity']}, and the wind speed is {data['current']['wind_mph']} mph" )

