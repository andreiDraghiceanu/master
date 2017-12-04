import requests
from flask import Flask, render_template, request, jsonify
from pprint import pprint

cities = ['New York', 'Paris', 'London']
city = 'CityName'


def main():
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c4dcf21ad47a1978dd438f51e5d21212')
    weather = response.json()
    # pprint(weather)
    print("The weather for", weather['name'] + ' is:')
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])

for city in cities[:]:
    main()

if __name__ == '__main__':
    pass




