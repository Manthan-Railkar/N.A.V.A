import requests

API_KEY = "c9451e57162ef769db79f5a47916bd93"  


def weather_report(data):
    try:
        if "weather" in data and "main" in data:
            w_r = data['weather'][0]["main"]
            desc = data['weather'][0]["description"]
            temp = data['main']['temp']
            city = data.get("name", "Unknown City")
            return f"The weather in {city} is {w_r.lower()} ({desc}), with a temperature of {temp}°C."
        elif "message" in data:
           \
            return f"Weather API error: {data['message']}"
        else:
            return "Could not fetch weather data. Please try again."
    except Exception as e:
        return f"Error processing weather data: {str(e)}"


def get_api_response(city):
    url = (
        f'https://api.openweathermap.org/data/2.5/weather?'
        f'q={city}&appid={API_KEY}&units=metric&lang=en'
    )
    return requests.get(url).json()


def get_data(city):
    response = get_api_response(city)
    return weather_report(response)
