
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# ---- Configuration ----
API_KEY = 'fbd870118698ca647f09'  # Replace with your actual OpenWeatherMap API key
CITY = 'Chennai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# ---- Fetch Weather Data ----
response = requests.get(URL)
data = response.json()

# Check for error
if data.get('cod') != '200':
    print("Failed to fetch data:", data.get('message', 'Unknown error'))
    exit()

# ---- Process Data ----
dates = []
temps = []
humidity = []

for entry in data['list']:
    dt = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    if dt.hour == 12:  # Only fetch data for 12PM each day
        dates.append(dt.date())
        temps.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

# ---- Plot Temperature ----
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker='o', linestyle='-', color='skyblue', label='Temperature (°C)')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()

# ---- Plot Humidity ----
plt.figure(figsize=(10, 5))
plt.bar(dates, humidity, color='orange', label='Humidity (%)')
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("humidity_plot.png")
plt.show()
