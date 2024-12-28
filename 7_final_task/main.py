import datetime
import os
from operator import truediv
from typing import Protocol
from pre_commit.output import write_line
import requests
import geocoder
import json
from functions import *
from consts import *


"""
Текущее время: 2023-10-03 09:48:47+03:00
Название города: Санкт-Петербург
Погодные условия: облачно
Текущая температура: 12 градусов по цельсию
Ощущается как: 11 градусов по цельсию
Скорость ветра: 5 м/c
"""

def __main__ ():
    program_activity = True
    while program_activity:
        print ("Введите название города, погоду в котором хотите узнать\nИли введите 0, если хотите завершить программу\n")
        sity: str
        sity = input()
        if sity == "0":
            program_activity = False
            continue






def print_weather_of_city (weather: dict):
    print (f"Текущее время: {weather["time"]}\n")
    print (f"Название города: {weather["city"]}\n")
    print (f"Погодные условия: {weather["weather_conditions"]}\n")
    print (f"Текущая температура: {weather["temperature"]} градусов по цельсию\n")
    print (f"Ощущается как: {weather["temperature_feels"]} градусов по цельсию\n")
    print (f"Скорость ветра: {weather["wind_speed"]} м/c\n")












BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


def generate_url(city: str):
    return BASE_URL + "appid=" + API_KEY + "&q=" + city + "&lang=ru" + "&units=metric"


def get_user_city():
    return geocoder.ip("me").city


def save_weather_data(weather_data):
    with open('wd.json', 'a') as file:
        json.dump(weather_data.data, file, indent=0)


def parse_weather_data(resp):
    try:
        timezone = datetime.timezone(datetime.timedelta(seconds=float(resp["timezone"])))
        time = datetime.datetime.fromtimestamp(float(resp["dt"]), timezone)
    except KeyError:
        time = resp["time"]
        # для чтения из json
    name = resp["name"]
    description = resp["weather"][0]["description"]
    temp_celsius = resp["main"]["temp"]
    feels_like_celsius = resp["main"]["feels_like"]
    speed = resp["wind"]["speed"]
    weatherdata = WeatherData(time, name, description, temp_celsius, feels_like_celsius, speed)
    return weatherdata


def weather_for_selected_city():
    city = input("Введите город:\n").replace(" ", "")
    url = generate_url(city)
    response = requests.get(url).json()
    if response["cod"] == 200:
        weatherdata = parse_weather_data(response)
        save_weather_data(weatherdata)
        print(weatherdata, "\n")
    else:
        print(f"Ошибка {response['cod']}: {response['message']}")


def weather_for_user_city():
    city = get_user_city()
    url = generate_url(city)
    response = requests.get(url).json()
    weatherdata = parse_weather_data(response)
    save_weather_data(weatherdata)
    print(weatherdata, "\n")




    def read_history():
        try:
            n = int(input("Сколько запросов?\n"))
            weather_datas = read_weather_data(n)
            weather_datas.reverse()
            for wd in weather_datas:
                wdprint = WeatherData(*wd.values())
                print(f"{wdprint}\n")
                del wdprint
        except ValueError:
            print('Число запросов выражается целым положительным числом')

    def read_weather_data(n: int):
        if (type(n) != int) or (n < 1):
            raise ValueError
        else:
            data_array = []
            with open('wd.json', 'r') as file:
                remainder = file.read().replace("\n", "")
                while len(remainder) > 2:
                    data_array.append(remainder.partition("}")[0] + "}")
                    remainder = remainder.partition("}")[2]
            weather_data_array = []
            i = 1
            data_array.reverse()
            for d in data_array:
                if i > n:
                    break
                js = json.loads(d)
                weather_data_array.append(js)
                i = i + 1
            return weather_data_array

    def clear_history():
        with open("wd.json", "w") as file:
            pass

    options = {"1": weather_for_user_city,
               "2": weather_for_selected_city,
               "3": read_history,
               "4": clear_history,
               "5": ""}

    def enable_cycle():
        while True:
            answer = input(answer_prompt).replace(" ", "")
            if answer in options.keys():
                if answer == "5":
                    break
                else:
                    options[answer]()
            else:
                print('Нет такой опции')

    if __name__ == "__main__":
        enable_cycle()