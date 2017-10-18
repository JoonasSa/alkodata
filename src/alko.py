import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
jyvaskyla_temp = weather_df['Jyvaskyla_rain'].iloc[::-1]
jyvaskyla_rain = weather_df['Jyvaskyla_temp'].iloc[::-1]
sodankyla_temp = weather_df['Sodankyla_temp'].iloc[::-1]
sodankyla_rain = weather_df['Sodankyla_rain'].iloc[::-1]
seinajoki_temp = weather_df['Seinajoki_temp'].iloc[::-1]
seinajoki_rain = weather_df['Seinajoki_rain'].iloc[::-1]

#Create a month of year x-axis
graph_months = (month.apply(lambda x: x[:2]))
graph_months[54] = graph_months[54] + "\n2013"
graph_months[44] = graph_months[44] + "\n2014"
graph_months[32] = graph_months[32] + "\n2015"
graph_months[20] = graph_months[20] + "\n2016"
graph_months[8] = graph_months[8] + "\n2017"
y_pos = np.arange(len(graph_months))

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

N = 55 #num of months
men_means = (20, 35, 30, 35, 27)
#men_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(y_pos, total, width, color='r')#, yerr=men_std)

women_means = (25, 32, 34, 20, 25)
#women_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(y_pos + width, helsinki_temp, width, color='b')#, yerr=women_std)

# add some text for labels, title and axes ticks
#ax.set_ylabel('Scores')
#ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(graph_months)

ax.legend((rects1[0], rects2[0]), ('Total', 'Temp'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()