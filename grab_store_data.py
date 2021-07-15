# Tanner Fry
# Goals:
# 1. Gather weather data from Rolla and visualize.
# 2. Gather weather data from around Rolla and visualize.
# Resources:
# 1. https://matplotlib.org/tutorials/introductory/pyplot.html

# Imports
import datetime
import pyowm
import threading
import time


def main():
    try:
        work_weather()
    except Exception as e:
        print(e)
        main()


# Weather
def work_weather():
    # Rolla City Weather ID's
    # 4406282, 5061159
    # reg.ids_for(matching='like'), reg.locations_for, reg.geopoints_for
    owm = pyowm.OWM('d1ad022124fbea23822145211a8085a7')
    observation = owm.weather_at_zip_code('65401', 'US')
    weather = observation.get_weather()

    # Record temperature
    file = 'rolla_data.txt'  # TODO: Fix hardcode
    timestamp = time.mktime(datetime.datetime.now().timetuple())
    temp_dict = weather.get_temperature('fahrenheit')

    with open(file, 'a') as file:
        file.write(str(timestamp) + ' ' +
                   str(temp_dict['temp']) + ' ' + str(temp_dict['temp_max']) + ' ' + str(temp_dict['temp_min']) + '\n')

    # Set up timer to continue gathering information
    threading.Timer(1200, work_weather).start()  # 1800 secs = 30 mins


if __name__ == '__main__':
    main()
