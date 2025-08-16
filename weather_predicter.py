import requests 

def weather_report(response): 
    data = response.json() 
    w_r = data['weather'][0]["main"]
    desc = data['weather'][0]["description"]
    temp = data['main']['temp']
    print(w_r)
    print(desc)
    print(temp)

def get_api_response(city,unit,language):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c9451e57162ef769db79f5a47916bd93&units={unit}&lang={language}'
    res = requests.get(url)
    return res 

def get_data(): 
    city = input("Enter the city name to get the weather report :") 
    unit = input("Enter the units in which you want the report: ")
    language = input("Enter your preferred language code as per: ")

    response = get_api_response(city,unit,language) 
    weather_report(response) 

get_data()