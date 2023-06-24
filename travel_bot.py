import requests
import json

# APIs
weather_api_key = "YOUR_WEATHER_API_KEY"

restaurant_api_key = "YOUR_RESTAURANT_API_KEY"
hotel_api_key = "YOUR_HOTEL_API_KEY"
translate_api_key = "YOUR_TRANSLATE_API_KEY"
currency_api_key = "YOUR_CURRENCY_API_KEY"
safety_api_key = "YOUR_SAFETY_API_KEY"

def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["cod"] != "404":
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"The weather in {city} is {weather} with a temperature of {temperature} K."
        else:
            return "City not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_restaurants(city):
    base_url = f"API_ENDPOINT_HERE?api_key={restaurant_api_key}&city={city}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["status"] == "OK":
            restaurants = data["restaurants"]
            restaurant_names = [restaurant["name"] for restaurant in restaurants]
            return f"Popular restaurants in {city}: {', '.join(restaurant_names)}"
        else:
            return "No restaurants found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_hotels(city):
    base_url = f"API_ENDPOINT_HERE?api_key={hotel_api_key}&city={city}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["status"] == "OK":
            hotels = data["hotels"]
            hotel_names = [hotel["name"] for hotel in hotels]
            return f"Popular hotels in {city}: {', '.join(hotel_names)}"
        else:
            return "No hotels found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_languages(city):
    base_url = f"API_ENDPOINT_HERE?api_key={translate_api_key}&city={city}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["status"] == "OK":
            languages = data["languages"]
            language_names = [language["name"] for language in languages]
            return f"Languages spoken in {city}: {', '.join(language_names)}"
        else:
            return "No language information found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_currency(city):
    base_url = f"API_ENDPOINT_HERE?api_key={currency_api_key}&city={city}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["status"] == "OK":
            currency = data["currency"]
            return f"The currency in {city} is {currency}"
        else:
            return "No currency information found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_safety_measures(city):
    base_url = f"API_ENDPOINT_HERE?api_key={safety_api_key}&city={city}"

    try:
        response = requests.get(base_url)
        data = json.loads(response.text)
        if data["status"] == "OK":
            safety_measures = data["safety_measures"]
            return f"Safety measures in {city}: {safety_measures}"
        else:
            return "No safety information found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def travel_chatbot():
    print("Welcome to the Travel Chatbot!")
    while True:
        user_input = input("Enter a city name (or 'quit' to exit): ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        else:
            print(get_weather(user_input))
            print(get_restaurants(user_input))
            print(get_hotels(user_input))
            print(get_languages(user_input))
            print(get_currency(user_input))
            print(get_safety_measures(user_input))


if __name__ == "__main__":
    travel_chatbot()
