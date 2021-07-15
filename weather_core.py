# Tanner Fry
# Goals:
# 1. Gather weather data from Rolla and visualize.
# 2. Gather weather data from around Rolla and visualize.
# Resources:
# 1. https://matplotlib.org/tutorials/introductory/pyplot.html

# Imports
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pyowm
import threading
import time


def main():
    # work_weather()
    # visualize_data('rolla', 'weather')
    # r_n_d_visualize('rolla', 'weather')

    exiting = False
    list_commands = ['EXIT', 'VISUALIZE']
    for command in list_commands:
        print(command)
    while exiting is False:
        command = input('Command: ')
        if command.upper() in list_commands:
            if 'EXIT' in command.upper():
                exiting = True
            elif 'VISUALIZE' in command.upper():
                visualize_data('rolla')  # TODO: Fix hardcode


# Visualize
def visualize_data(location: str):
    """
    A visualization of the supplied data by plotting points on temperature at a given time within a given location.

    :param location: town name for the data file
    :type location: str
    :return: none
    :rtype: none
    """
    # Load data with numpy
    times_new = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[0])
    times_new = [datetime.datetime.fromtimestamp(time) for time in times_new]
    degrees_reg = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[1])
    degrees_max = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[2])  # Could use later
    degrees_min = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[3])  # Could use later

    # Setup plotting with matlab
    plt.title('Rolla Data Degrees Over Time')
    plt.xlabel('Time (D:H)')
    plt.ylabel('Degrees')
    plt.plot(times_new, degrees_reg, 'b-', times_new, degrees_reg, 'ro')

    # Display
    plt.show()


# Research and development
def r_n_d_visualize(location: str):
    """
    A 'research and development' visualization of the supplied data by plotting points on temperature at a given time
    within a given location.

    :param location: the city/town of the weather station
    :type location: str
    :return: none
    :rtype: none
    """
    # Load data with numpy
    time = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[0])
    degrees_reg = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[1])
    degrees_max = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[2])
    degrees_min = np.loadtxt(location + '_data.txt', delimiter=' ', usecols=[3])

    # Setup plotting with matplot
    plt.figure(1, figsize=(9, 3))
    plt.subplot(131)
    plt.bar(time, degrees_reg)
    plt.subplot(132)
    plt.scatter(time, degrees_reg)
    plt.subplot(133)
    plt.plot(time, degrees_reg)
    plt.suptitle('Rolla Data Degrees Over Time')
    plt.xlabel('Time Unix')
    plt.ylabel('Degrees')

    # Display
    plt.show()


if __name__ == '__main__':
    main()
