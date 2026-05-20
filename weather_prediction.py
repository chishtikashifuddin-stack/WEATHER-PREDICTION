import requests
import json

print("*----------------------------------------*")
print("|WELCOME TO SEE THE WEATHER OF YOURE CITY|")
print("*----------------------------------------*")

def fun():
    city = input("Enter city name: ")
    api_key = "406560f55b7337c453c4480373f9dbe6"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    # print(data)
    if "main" in data: 
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        sea = data["main"]["sea_level"]
        lon = data["coord"]["lon"]
        lat = data["coord"]["lat"]
        wind = data["wind"]["speed"]
        Feel = data["main"]["feels_like"] 
        pressure = data["main"]["pressure"]
        tem_min = data["main"]["temp_min"]
        tem_max = data["main"]["temp_max"]
        id = data["sys"]["id"]
        sunrise = data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]
        time_zone = data["timezone"]
        cod = data["cod"]
        visi = data["visibility"]
        fun1(city, temp, weather, humidity,sea,lon,wind,lat,Feel,tem_max,tem_min,id,sunrise,sunset,time_zone,cod,pressure,visi)
    
    else:
        print("*-------------------------*")
        print("|PLEASE ENTER CORRECT CITY|")
        print("*-------------------------*\n")
        fun()

def fun1(city, temp, weather, humidity,sea,lon,wind,lat,Feel,tem_max,tem_min,id,sunrise,sunset,time_zone,cod,pressure,visi):
    print("\n*-------------------------------------------------*")
    print("                    *----------------*                ")
    print(f"                    | WEATHER REPORT |                ")
    print("                    *----------------*               \n")
    print(f"                    CITY: {city}                       ")
    print(f"                    TEMPERATURE: {temp} °C             ")
    print(f"                    WEATHER: {weather}                 ")
    print(f"                    SEA_LEVEL : {sea}                  ") 
    print(f"                    LONGITUDE : {lon}                  ")
    print(f"                    LATITUDE : {lat}                   ")
    print(f"                    WIND SPEED : {wind}%               ")
    print(f"                    HUMIDITY : {humidity}%             ")
    print(f"                    FEEL LIKE : {Feel}%                ")
    print(f"                    PRESSURE : {pressure}%             ")
    print(f"                    SUNRISE : {sunrise}                ")
    print(f"                    SUNSET : {sunset}                  ")
    print(f"                    TIME_ZONE : {time_zone}            ")
    print(f"                    VISIBILITY : {visi}                 ")
    print(f"                    COD : {cod}                        ")
    print("*---------------------------------------------------*\n")
    fun()
    
fun()