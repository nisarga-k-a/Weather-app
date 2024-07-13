from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = '330e7775765ee75f5be2d98f71b8c2d3'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    temp = None
    error = None
    if request.method == 'POST':
        user_input = request.form['city']
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
        
        response_json = weather_data.json()
        
        if response_json.get('cod') == '404':
            error = "No City Found"
        elif response_json.get('cod') == 200:
            weather = response_json['weather'][0]['main']
            temp = round(response_json['main']['temp'])
        else:
            error = response_json.get('message', 'Unknown error')
    
    return render_template('index.html', weather=weather, temp=temp, error=error)

if __name__ == '__main__':
    app.run(debug=True)
