import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read alko_sales.csv
alko_df = pd.read_csv("alko_sales.csv")

#Invert and assign the months with data available to a variable
month = alko_df['Month'].iloc[::-1]

#Invert and assign all alko sales columns to a variable for easy access
vodka_spirit = alko_df['VodkaAndSpirit'].iloc[::-1]
other_spirit = alko_df['OtherSpirit'].iloc[::-1]
fortified_wine = alko_df['FortifiedWine'].iloc[::-1]
red_wine = alko_df['RedWine'].iloc[::-1]
white_wine = alko_df['WhiteWine'].iloc[::-1]
sparkling_wine = alko_df['SparklingWine'].iloc[::-1]
rose_wine = alko_df['RoseWine'].iloc[::-1]
other_wine = alko_df['OtherWine'].iloc[::-1]
cider = alko_df['Cider'].iloc[::-1]
long_drink = alko_df['LongDrink'].iloc[::-1]
beer = alko_df['Beer'].iloc[::-1]
non_alcoholic_beverage = alko_df['NonAlcoholicBeverage'].iloc[::-1]
total = alko_df['Total'].iloc[::-1]
pure_alcohol_total = alko_df['PureAlcoholTotal'].iloc[::-1]

#Read weather_stat.csv
weather_df = pd.read_csv("weather_stat.csv")

#Invert and assing all weather statistic columns to a variable for easy access
helsinki_temp = weather_df['Helsinki_temp'].iloc[::-1]
helsinki_rain = weather_df['Helsinki_rain'].iloc[::-1]
jyvaskyla_temp = weather_df['Jyvaskyla_rain'].iloc[::-1]
jyvaskyla_rain = weather_df['Jyvaskyla_temp'].iloc[::-1]
sodankyla_temp = weather_df['Sodankyla_temp'].iloc[::-1]
sodankyla_rain = weather_df['Sodankyla_rain'].iloc[::-1]
seinajoki_temp = weather_df['Seinajoki_temp'].iloc[::-1]
seinajoki_rain = weather_df['Seinajoki_rain'].iloc[::-1]

#Plot vodka sales per month
graph_months = (month.apply(lambda x: x[:2]))
y_pos = np.arange(len(graph_months))

plt.bar(y_pos, vodka_spirit, align='center', alpha=0.5)
plt.xticks(y_pos, graph_months)
plt.ylabel('1000 litres of vodka and spirits sold')
plt.xlabel('Month')
plt.title('Vodka and spirit sales in ton litres per month')

plt.show()

#Plot temperature per month in Helsinki
plt.bar(y_pos, helsinki_temp, align='center', alpha=0.5)
plt.xticks(y_pos, graph_months)
plt.ylabel('Average temperature in Helsinki')
plt.xlabel('Month')
plt.title('Average temeperature in Helsinki per month')

plt.show()