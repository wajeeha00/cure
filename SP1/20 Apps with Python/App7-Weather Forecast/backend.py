API_KEY ="8fbc5d97fce6b6cb7b7ad5fbdfe0212f"
import requests
# URL = "api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
def get_data(place, forecast_Days = None):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_Days
    filtered_data = filtered_data[:nr_values]        
    return filtered_data