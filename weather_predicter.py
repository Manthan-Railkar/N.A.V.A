import requests 

def weather_report(response): 
    data = response.json() 
    w_r = data['weather'][0]["main"]
    desc = data['weather'][0]["description"]
    temp = data['main']['temp']
    
    return desc
    

def get_api_response(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9451e57162ef769db79f5a47916bd93&units=me&lang=en'
    res = requests.get(url)
    return res 

def get_data(city): 
    city = city
   

    response = get_api_response(city) 
    return weather_report(response) 
    

