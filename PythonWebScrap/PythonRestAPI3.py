from flask import Flask, render_template, request
import requests

app = Flask(__name__)
zipcode = ''


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + '&appid=c4dcf21ad47a1978dd438f51e5d21212')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    return str(temp_k)
    # return render_template('tempreture.html')


@app.route('/')
def index():
    return render_template('index.html')

zipcode = input('Please insert the zipcode of the city: ')

if __name__ == '__main__':
    app.run(debug=True)

