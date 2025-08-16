import requests 

def weather_report(response): 
    data = response.json() 
    w_r = data['weather'][0]["main"]
    desc = data['weather'][0]["description"]
    temp = data['main']['temp']
    return w_r,desc,temp 

def get_api_response(city,unit,language):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9451e57162ef769db79f5a47916bd93&units={unit}&lang={language}'
    res = requests.get(url)
    return res 

def get_data(city): 
    city =city 
    unit ='me'
    language ='en'

    response = get_api_response(city,unit,language) 
    weather_report(response) 

