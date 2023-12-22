from flask import Flask
import requests
import json

app = Flask(__name__)
@app.route("/weather", methods=["GET"])
def display_weather():
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

    r = requests.get(url)

    weather_details = r.json()

    for key in weather_details:
        print(key, ":", weather_details[key])
    return weather_details["current"] 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
