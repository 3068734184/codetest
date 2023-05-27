import requests
import json

def get_weather(city):
    api_key = "YOUR_API_KEY"  # 替换为您的OpenWeatherMap API密钥
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(base_url)
    data = json.loads(response.text)

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found.")

# 主程序
if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
