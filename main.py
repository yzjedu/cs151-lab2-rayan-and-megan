# Programmers: Megan, Krishon, Korede, Rayan
# Course: Cs151, Professor Zee
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem statement: Create a program that will determine the expected population in the future /
# (a certain number of years away) for a country based on a current population amount if you are /
# given (1) how often someone is born (in seconds), (2) how often someone dies (in seconds), and /
# (3) how often a new immigrant joins the country (in seconds).

# Data In: Code needs input on how many seconds between birth, how many seconds between death, how /
# many seconds between immigrations, what the current population is, how many years in the future you want to see
# Data Out: The population change and if the population increased, decreased or is the same

# User should be prompted to enter five inputs: seconds before birth, seconds between death,/
# seconds between immigration current population size, and number of years in the future.

sec_year = 31536000
print("How many seconds between birth?")
secs_births = float(input())
print("How many seconds between death?")
secs_deaths = float(input())
print("How many seconds between immigrations?")
secs_immigrations = float(input())
print("What is the current population?")
population = float(input())
print("How many years in the future?")
num_years = float(input())

# Code should calculate population change and print it.
pop_change = ((sec_year/secs_births + sec_year/secs_immigrations - sec_year/secs_deaths) * num_years)
print("The population change is", pop_change, 'people')

# Code should calculate future population and print it.
future_pop = (population + pop_change)
print("The future population is", future_pop, 'people')

# Code should use "if" statement to compare results of/
# population change and future calculation to output various statements

if future_pop > population:
    print('increased population')
elif future_pop < population:
    print('decreased population')
else:
    print('same population')

