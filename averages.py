"""
    Made after discussion on what would be the correct way to calculate the average height of world population.
    - Would it be better to take a new round av measure everyone, or would it be enough to use
        the average from each country?

    This code allows you you plug in the number of people and number of countries
    to calculate with.
    Run this code with interactive window.

    Before running: 
    - What do you think the answer is?
    - And if so, how different do you think these methods are from eachother?
"""
import random
import numpy as np

heights = [] # rng height
people = 7487685 # nr of people
max_height = 200 # height ceiling, just to set a limit. not actually important
countries = 44 # nr countires to batch
country_avgs = [] # list to store avg height of each country

for i in range(people):
    heights.append(random.heights(0, 200))

def rawavg():
    print(np.mean(heights))

def printlist():
    print(heights)

def avgwithcountries():
    for i in range(0, len(heights), countries):
        country_avg = heights[i:i+countries]
        country_avgs.append(np.mean(country_avg))
    print(np.mean(country_avgs))

def printavgbatches():
    print(country_avgs)
