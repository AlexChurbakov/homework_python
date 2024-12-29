import datetime
import os
from operator import truediv
from pre_commit.output import write_line
import requests
import geocoder
import json


global_weather = {"time": "", "city": "", "weather_conditions": "", "temperature": "", "temperature_feels": "", "wind_speed": ""}
path = "weather_data_file.txt"


def main ():
    program_activity = True
    while program_activity:
        print ("""                  Введите: 0, если хотите завершить программу\n
                           1, чтоб узнать погоду в выбранном городе\n
                           2, чтоб узнать погоду в Вашем городе\n
                           3, чтоб посмотреть историю запросов\n
                           4, чтоб стереть историю запросов\n""")
        swithc_key = input()
        if swithc_key == "0":
            program_activity = False
            continue
        elif swithc_key == "1":
            get_weather_selected_sity()
        elif swithc_key == "2":
            get_weather_your_sity()
        elif swithc_key == "3":
            read_story_file()
        elif swithc_key == "4":
            clear_story_file()
        else:
            print ("Вы указали неверный вариант. Попробуйте ещё раз\n")
            continue


def get_URL(city: str):
    API_KEY = open("api_key.txt", "r").read()
    return "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&lang=ru&units=metric"


def print_weather_of_city (weather: dict):
    print (f"Текущее время: {weather["time"]}\n")
    print (f"Название города: {weather["city"]}\n")
    print (f"Погодные условия: {weather["weather_conditions"]}\n")
    print (f"Текущая температура: {weather["temperature"]} градусов по цельсию\n")
    print (f"Ощущается как: {weather["temperature_feels"]} градусов по цельсию\n")
    print (f"Скорость ветра: {weather["wind_speed"]} м/c\n")


def get_weather_selected_sity():
    city = input("Введите название города:\n").replace(" ", "")
    url = get_URL(city)
    response = requests.get(url).json()
    #print (response)
    if response["cod"] == 200:
        weather_info = write_weather_info(response)
        save_info_to_file(make_string(weather_info))
        print_weather_of_city(weather_info)
    else:
        print(f"Ошибка {response['cod']}: {response['message']}")


def get_weather_your_sity():
    city = geocoder.ip("me").city
    url = get_URL(city)
    response = requests.get(url).json()
    weather_info = write_weather_info(response)
    save_info_to_file(make_string(weather_info))
    print_weather_of_city(weather_info)


def read_story_file():
    if (not os.path.isfile(path) or os.path.getsize(path)) == 0:
        print ("Файл пуст или не существует\n")
        return
    try:
        n = int(input("Сколько последних запросов Вы хотите посмотреть?\n"))
        if (type(n) != int) or (n < 1):
            raise ValueError
        else:
            with open(path, 'r') as file:
                new_n = n
                while new_n >= 1:
                    for index in range(7):
                        file_info = file.readline()
                        if file_info == "":
                            print("Больше в файле нет информации\n")
                            return
                        print(file_info, "\n")
                    new_n -= 1
    except ValueError:
        print("Число запросов выражается целым положительным числом\n")


def clear_story_file():
    with open(path, "w") as file:
        pass


def save_info_to_file(file_info):
    if not os.path.isfile(path):
        create_file(path)
    with open(path, 'a') as file:
        file.write(file_info)


def create_file(path: str):
    with open(path, "w") as _:
        pass

def make_string(weather) -> str:
    file_info = f"\
    Текущее время: {weather["time"]}\n\
    Название города: {weather["city"]}\n\
    Погодные условия: {weather["weather_conditions"]}\n\
    Текущая температура: {weather["temperature"]} градусов по цельсию\n\
    Ощущается как: {weather["temperature_feels"]} градусов по цельсию\n\
    Скорость ветра: {weather["wind_speed"]} м/c\n"
    return file_info

def write_weather_info(resp):
    try:
        timezone = datetime.timezone(datetime.timedelta(seconds=float(resp["timezone"])))
        time = datetime.datetime.fromtimestamp(float(resp["dt"]), timezone)
    except KeyError:
        print("Ошибка\n")

    weather = global_weather
    weather["time"] = time
    weather["city"] = resp["name"]
    weather["weather_conditions"] = resp["weather"][0]["description"]
    weather["temperature"] = resp["main"]["temp"]
    weather["temperature_feels"] = resp["main"]["feels_like"]
    weather["wind_speed"] = resp["wind"]["speed"]
    return weather


if __name__ == "__main__":
    main()



# Сейчас файл читает всегда сначала, нужно сделать, чтоб читал с конца
# Добавить проверку пустоты файла вначале считывания




