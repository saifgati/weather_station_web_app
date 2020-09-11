from flask import Flask, render_template, request
from pip._vendor import requests

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    city1 = "london"
    city2 = "new york"
    city3 = "paris"
    city4 = "tunis"
    city5 = "Berlin"
    url_weather1 = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city1 + '&appid=0c2b40ce81103e261f0b56bc85b40dff')
    json_object1 = url_weather1.json()
    temp_k1 = float(json_object1['main']['temp'])
    clouds1 = json_object1['weather'][0]
    clouds1=clouds1["description"]
    temp_c1 = "%.2f" % (temp_k1 - 273.15)
    print(json_object1)

    url_weather2 = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city2 + '&appid=0c2b40ce81103e261f0b56bc85b40dff')
    json_object2 = url_weather2.json()
    temp_k2 = float(json_object2['main']['temp'])
    clouds2 = json_object2['weather'][0]
    clouds2 = clouds2["description"]
    temp_c2 = "%.2f" % (temp_k2 - 273.15)

    url_weather3 = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city3 + '&appid=0c2b40ce81103e261f0b56bc85b40dff')
    json_object3 = url_weather3.json()
    temp_k3 = float(json_object3['main']['temp'])
    clouds3 = json_object3['weather'][0]
    clouds3 = clouds3["description"]
    temp_c3 = "%.2f" % (temp_k3 - 273.15)

    url_weather4 = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city4 + '&appid=0c2b40ce81103e261f0b56bc85b40dff')
    json_object4 = url_weather4.json()
    temp_k4 = float(json_object4['main']['temp'])
    clouds4 = json_object4['weather'][0]
    clouds4 = clouds4["description"]
    temp_c4 = "%.2f" % (temp_k4 - 273.15)

    url_weather5 = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city5 + '&appid=0c2b40ce81103e261f0b56bc85b40dff')
    json_object5 = url_weather5.json()
    temp_k5 = float(json_object5['main']['temp'])
    clouds5 = json_object5['weather'][0]
    clouds5 = clouds5["description"]
    temp_c5 = "%.2f" % (temp_k5 - 273.15)
    return render_template('index.html', temp_c1= temp_c1,temp_c2=temp_c2,temp_c3=temp_c3,temp_c4=temp_c4,temp_c5=temp_c5, clouds1=clouds1,
                           clouds2=clouds2,clouds3=clouds3,clouds4=clouds4,clouds5=clouds5)


@app.route('/City', methods=['POST', 'GET'])
def City():
    return render_template('City.html')



if __name__ == '__main__':
    app.run()
