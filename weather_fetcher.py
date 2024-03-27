import requests
import os

def fetch_weather(api_key, city="Tbilisi"):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&aqi=no"
    # print(url)
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        simple_weather = {
            'city': city,
            'temperature': weather_data['current']['temp_c'],
            'condition': weather_data['current']['condition']['text'],
            'cloud': weather_data['current']['cloud'],
            'precipitation': weather_data['current']['precip_mm'],
            'high': weather_data['forecast']['forecastday'][0]['day']['maxtemp_c'],
            'low': weather_data['forecast']['forecastday'][0]['day']['mintemp_c'],
            'rain': weather_data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            'icon': "https:" + weather_data['current']['condition']['icon'],
        }
        print(simple_weather)
        return simple_weather
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None



# if __name__ == '__main__':
#     weather_api_key = os.getenv('WEATHER_API_KEY')
#     weather = fetch_weather(weather_api_key)


#     {"location":
#         {"name":"Tbilisi",
#         "region":"Dushet'is Raioni",
#         "country":"Georgia",
#         "lat":41.73,
#         "lon":44.79,
#         "tz_id":"Asia/Tbilisi",
#         "localtime_epoch":1711445199,
#         "localtime":"2024-03-26 13:26"},
#     "current":
#         {"last_updated_epoch":1711444500,
#         "last_updated":"2024-03-26 13:15",
#         "temp_c":6.0,
#         "temp_f":42.8,
#         "is_day":1,
#         "condition":
#             {"text":"Overcast",
#             "icon":"//cdn.weatherapi.com/weather/64x64/day/122.png",
#             "code":1009},
#         "wind_mph":24.2,
#         "wind_kph":38.9,
#         "wind_degree":320,
#         "wind_dir":"NW",
#         "pressure_mb":1008.0,
#         "pressure_in":29.77,
#         "precip_mm":0.04,
#         "precip_in":0.0,
#         "humidity":81,
#         "cloud":100,
#         "feelslike_c":1.9,
#         "feelslike_f":35.3,
#         "vis_km":10.0,
#         "vis_miles":6.0,
#         "uv":2.0,
#         "gust_mph":28.6,
#         "gust_kph":46.1}}

# ['forecast']['forecastday'][0]['day']['maxtemp_c']

# {"location":
#     {"name":"Tbilisi","region":"Dushet'is Raioni","country":"Georgia","lat":41.73,"lon":44.79,"tz_id":"Asia/Tbilisi","localtime_epoch":1711446229,"localtime":"2024-03-26 13:43"},
# "current":
#     {"last_updated_epoch":1711445400,"last_updated":"2024-03-26 13:30","temp_c":6.0,"temp_f":42.8,"is_day":1,"condition":{"text":"Overcast","icon":"//cdn.weatherapi.com/weather/64x64/day/122.png","code":1009},"wind_mph":24.2,"wind_kph":38.9,"wind_degree":320,"wind_dir":"NW","pressure_mb":1008.0,"pressure_in":29.77,"precip_mm":0.04,"precip_in":0.0,"humidity":81,"cloud":100,"feelslike_c":1.9,"feelslike_f":35.3,"vis_km":10.0,"vis_miles":6.0,"uv":2.0,"gust_mph":28.6,"gust_kph":46.1},
# "forecast":
#     {"forecastday":
#         [{"date":"2024-03-26",
#         "date_epoch":1711411200,
#         "day":
#                 {"maxtemp_c":9.8,
#                 "maxtemp_f":49.6,
#                 "mintemp_c":3.2,
#                 "mintemp_f":37.8,
#                 "avgtemp_c":5.7,
#                 "avgtemp_f":42.3,
#                 "maxwind_mph":21.0,
#                 "maxwind_kph":33.8,
#                 "totalprecip_mm":0.39,
#                 "totalprecip_in":0.02,
#                 "totalsnow_cm":0.0,
#                 "avgvis_km":9.7,
#                 "avgvis_miles":6.0,
#                 "avghumidity":65,
#                 "daily_will_it_rain":1,
#                 "daily_chance_of_rain":89,
#                 "daily_will_it_snow":0,
#                 "daily_chance_of_snow":0,
#                 "condition":
#                     {"text":"Patchy rain nearby",
#                     "icon":"//cdn.weatherapi.com/weather/64x64/day/176.png",
#                     "code":1063},
#                 "uv":3.0},
#         "astro":
#                 {"sunrise":"06:54 AM","sunset":"07:20 PM","moonrise":"08:35 PM","moonset":"07:19 AM","moon_phase":"Waning Gibbous","moon_illumination":100,"is_moon_up":1,"is_sun_up":0},
#         "hour":
#                 [{"time_epoch":1711396800,"time":"2024-03-26 00:00","temp_c":5.1,"temp_f":41.1,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":2.9,"wind_kph":4.7,"wind_degree":318,"wind_dir":"NW","pressure_mb":1007.0,"pressure_in":29.74,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":74,"cloud":16,"feelslike_c":4.3,"feelslike_f":39.7,"windchill_c":4.3,"windchill_f":39.7,"heatindex_c":5.1,"heatindex_f":41.1,"dewpoint_c":0.8,"dewpoint_f":33.5,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":4.6,"gust_kph":7.3,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711400400,"time":"2024-03-26 01:00","temp_c":4.9,"temp_f":40.8,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":3.6,"wind_kph":5.8,"wind_degree":326,"wind_dir":"NNW","pressure_mb":1007.0,"pressure_in":29.74,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":71,"cloud":19,"feelslike_c":3.7,"feelslike_f":38.7,"windchill_c":3.7,"windchill_f":38.7,"heatindex_c":4.9,"heatindex_f":40.8,"dewpoint_c":0.2,"dewpoint_f":32.3,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.6,"gust_kph":9.1,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711404000,"time":"2024-03-26 02:00","temp_c":4.5,"temp_f":40.1,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":4.0,"wind_kph":6.5,"wind_degree":330,"wind_dir":"NNW","pressure_mb":1007.0,"pressure_in":29.75,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":72,"cloud":15,"feelslike_c":3.0,"feelslike_f":37.4,"windchill_c":3.0,"windchill_f":37.4,"heatindex_c":4.5,"heatindex_f":40.1,"dewpoint_c":-0.0,"dewpoint_f":32.0,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":6.2,"gust_kph":10.0,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711407600,"time":"2024-03-26 03:00","temp_c":4.1,"temp_f":39.3,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":4.3,"wind_kph":6.8,"wind_degree":327,"wind_dir":"NNW","pressure_mb":1008.0,"pressure_in":29.75,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":73,"cloud":18,"feelslike_c":2.4,"feelslike_f":36.3,"windchill_c":2.4,"windchill_f":36.3,"heatindex_c":4.1,"heatindex_f":39.3,"dewpoint_c":-0.4,"dewpoint_f":31.3,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":6.5,"gust_kph":10.4,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711411200,"time":"2024-03-26 04:00","temp_c":4.0,"temp_f":39.1,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":3.6,"wind_kph":5.8,"wind_degree":332,"wind_dir":"NNW","pressure_mb":1007.0,"pressure_in":29.75,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":70,"cloud":19,"feelslike_c":2.6,"feelslike_f":36.7,"windchill_c":2.6,"windchill_f":36.7,"heatindex_c":4.0,"heatindex_f":39.1,"dewpoint_c":-0.9,"dewpoint_f":30.3,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.3,"gust_kph":8.6,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711414800,"time":"2024-03-26 05:00","temp_c":3.6,"temp_f":38.6,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":3.6,"wind_kph":5.8,"wind_degree":338,"wind_dir":"NNW","pressure_mb":1007.0,"pressure_in":29.74,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":68,"cloud":12,"feelslike_c":2.3,"feelslike_f":36.1,"windchill_c":2.3,"windchill_f":36.1,"heatindex_c":3.7,"heatindex_f":38.6,"dewpoint_c":-1.7,"dewpoint_f":29.0,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.5,"gust_kph":8.9,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711418400,"time":"2024-03-26 06:00","temp_c":3.5,"temp_f":38.3,"is_day":0,"condition":{"text":"Clear ","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":3.6,"wind_kph":5.8,"wind_degree":322,"wind_dir":"NW","pressure_mb":1007.0,"pressure_in":29.74,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":67,"cloud":9,"feelslike_c":2.1,"feelslike_f":35.7,"windchill_c":2.1,"windchill_f":35.7,"heatindex_c":3.5,"heatindex_f":38.3,"dewpoint_c":-2.1,"dewpoint_f":28.2,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.5,"gust_kph":8.9,"uv":1.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711422000,"time":"2024-03-26 07:00","temp_c":3.2,"temp_f":37.8,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":3.4,"wind_kph":5.4,"wind_degree":331,"wind_dir":"NNW","pressure_mb":1008.0,"pressure_in":29.75,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":66,"cloud":7,"feelslike_c":1.9,"feelslike_f":35.5,"windchill_c":1.9,"windchill_f":35.5,"heatindex_c":3.2,"heatindex_f":37.8,"dewpoint_c":-2.5,"dewpoint_f":27.5,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.2,"gust_kph":8.4,"uv":2.0,"short_rad":0.0,"diff_rad":0.0},
#                 {"time_epoch":1711425600,"time":"2024-03-26 08:00","temp_c":4.3,"temp_f":39.8,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":2.7,"wind_kph":4.3,"wind_degree":327,"wind_dir":"NNW","pressure_mb":1008.0,"pressure_in":29.76,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":62,"cloud":25,"feelslike_c":3.6,"feelslike_f":38.5,"windchill_c":3.6,"windchill_f":38.5,"heatindex_c":4.3,"heatindex_f":39.8,"dewpoint_c":-2.4,"dewpoint_f":27.8,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":3.4,"gust_kph":5.5,"uv":2.0,"short_rad":16.64,"diff_rad":5.5},
#                 ...]]