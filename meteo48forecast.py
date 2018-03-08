import urllib2
from bs4 import BeautifulSoup

city = "Kaunas"

response = urllib2.urlopen("http://www.meteo.lt/lt/miestas?placeCode=" + city)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
weather_info = soup.find_all('table', class_='hourly_weather') # 48 hour forecast

time_var = []
temperature_var = []
feellike_var = []
winddirection_var = []
windspeed_var = []
windgust_var = []
precipitation_var = []
pressure_var = []
humidity_var = []
condition_var = []

# We want to find all 48 hour information.
for w in weather_info:
		time = w.find_all(class_='forecastTime hidden')
		temperature = w.find_all(class_='temperature')
		feellike = w.find_all(class_='feelLike')
		winddirection = w.find_all(class_='windDirectionGroundDegree hidden')
		windspeed = w.find_all(class_='windSpeedGround')
		windgust = w.find_all(class_='windGustGround')
		precipitation = w.find_all(class_='precipitation')
		pressure = w.find_all(class_='pressureMeanSea')
		humidity = w.find_all(class_='humidityGround')
		condition = w.find_all(class_='conditionText hidden')
		
		for ti in time:
			time_var += ti.strings

		for te in temperature:
			temperature_var += te.strings

		for fe in feellike:
			feellike_var += fe.strings

		for wd in winddirection:
			winddirection_var += wd.strings

		for ws in windspeed:
			windspeed_var += ws.strings

		for wg in windgust:
			windgust_var += wg.strings

		for prec in precipitation:
			precipitation_var += prec.strings

		for pres in pressure:
			pressure_var += pres.strings

		for hum in humidity:
			humidity_var += hum.strings

		for con in condition:
			condition_var += con.strings

i=0

for t in time_var:
	# we need wind from where it blows
	wind_modulus = (float(winddirection_var[i]) + 180) % 360
	windcode_var = round(wind_modulus/45+1)

	print(time_var[i] + '\tTemperature:' + temperature_var[i] +  '\tFeels like:' + feellike_var[i] + '\tWind code:' + str(int(windcode_var)) + '\tWind from:' + str(int(wind_modulus)) + '\tWind speed:' + windspeed_var[i] + '\tWind gust:' + windgust_var[i] + '\tPrecipitation:' + precipitation_var[i] + '\tPressure:' + pressure_var[i] + '\tHumidity:' + humidity_var[i] + '\tCondition:' + condition_var[i])
	i += 1
