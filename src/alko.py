import numpy as np
import pandas as pd
from graph_utils import create_two_bar_graph, dataframe_mean

#Alko data
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

#Weather data
weather_df = pd.read_csv("weather_stat.csv")

#Invert and assign all weather statistic columns to a variable for easy access
helsinki_temp = weather_df['Helsinki_temp'].iloc[::-1]
helsinki_rain = weather_df['Helsinki_rain'].iloc[::-1]
jyvaskyla_temp = weather_df['Jyvaskyla_temp'].iloc[::-1]
jyvaskyla_rain = weather_df['Jyvaskyla_rain'].iloc[::-1]
sodankyla_temp = weather_df['Sodankyla_temp'].iloc[::-1]
sodankyla_rain = weather_df['Sodankyla_rain'].iloc[::-1]
seinajoki_temp = weather_df['Seinajoki_temp'].iloc[::-1]
seinajoki_rain = weather_df['Seinajoki_rain'].iloc[::-1]

#Average temp and rain per month in Finland
finland_temp = dataframe_mean([helsinki_temp, jyvaskyla_temp, sodankyla_temp, seinajoki_temp])
finland_temp = finland_temp[0].iloc[::-1]
finland_rain = dataframe_mean([helsinki_rain, jyvaskyla_rain, sodankyla_rain, seinajoki_rain])
finland_rain = finland_rain[0].iloc[::-1]

#Create a month of year x-axis
graph_months = (month.apply(lambda x: x[:2]))
graph_months[54] = graph_months[54] + "\n2013"
graph_months[44] = graph_months[44] + "\n2014"
graph_months[32] = graph_months[32] + "\n2015"
graph_months[20] = graph_months[20] + "\n2016"
graph_months[8] = graph_months[8] + "\n2017"
x_pos = np.arange(len(graph_months))

#Graph total alcohol sold and average temperature in Helsinki
create_two_bar_graph(total.apply(lambda x: x / 1000), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Total alcohol sold and average celcius degrees per month',
                     y_label='1000000 litres of alcohol sold and average celcius',
                     a_legend="1000 litres of alcohol sold", b_legend="Average temperature", autolabel1=True)

'''
#Plot vodka sales per month
plt.bar(y_pos, vodka_spirit, align='center', alpha=0.5)
plt.xticks(y_pos, graph_months)
plt.ylabel('1000 litres of vodka and spirits sold')
plt.xlabel('Year and month')
plt.title('Vodka and spirit sales in thousand litres per month')

plt.show()

#Plot temperature per month in Helsinki
plt.bar(y_pos, helsinki_temp, align='center', alpha=0.5)
plt.xticks(y_pos, graph_months)
plt.ylabel('Average celsius in Helsinki')
plt.xlabel('Year and month')
plt.title('Average temperature in Helsinki per month')

plt.show()
'''