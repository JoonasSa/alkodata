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
finland_temp = finland_temp[0]
finland_rain = dataframe_mean([helsinki_rain, jyvaskyla_rain, sodankyla_rain, seinajoki_rain])
finland_rain = finland_rain[0]

#Create a month of year x-axis
graph_months = (month.apply(lambda x: x[:2]))
graph_months[54] = graph_months[54] + "\n2013"
graph_months[44] = graph_months[44] + "\n2014"
graph_months[32] = graph_months[32] + "\n2015"
graph_months[20] = graph_months[20] + "\n2016"
graph_months[8] = graph_months[8] + "\n2017"
x_pos = np.arange(len(graph_months))
rain_x_pos = np.arange(31,55)

celsius_string = "$^\circ$C"

#Graph of total alcohol sold and average temperature in Finland
create_two_bar_graph(total.apply(lambda x: x / 1000), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Total alcohol sold and average temperature per month',
                     #y_label='1000000 litres of alcohol sold and average celcius',
                     a_legend="1000000 l of alcohol sold", b_legend="Average temperature in " + celsius_string, autolabel1=True, autolabel1decimal=True)

#Graph of total alcohol sold and average temperature and rain in Finland from 10/2015 (index 31) onward
#months_ = x_tick_labels = graph_months[31:]
create_two_bar_graph(total[31:].apply(lambda x: x / 1000), finland_temp[31:], rain_x_pos,
                     x_tick_labels=graph_months,
                     title='Total alcohol sold, average temperature and rain per month',
                     #y_label='1000000 l of alcohol sold and average celcius and cl rain',
                     c=finland_rain[31:].apply(lambda x: x / 10),
                     a_legend="1000000 l of alcohol sold", b_legend="Average temperature in " + celsius_string,
                     c_legend="Average rain in cl", autolabel1=True, autolabel1decimal=True)

#Graph of vodka and spirits sold and average temperature in Finland
create_two_bar_graph(vodka_spirit.apply(lambda x: x / 100), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Vodka and spirits sold and average temperature per month',
                     #y_label='100000 litres of vodka and spirits sold and average celcius',
                     a_legend="100000 l of vodka and spirits sold", b_legend="Average temperature in " + celsius_string)
#=> The sales spike during christmas and new years eve. Otherwise they are rather constant

#Graph of sparkling wines sold and average temperature in Finland
create_two_bar_graph(sparkling_wine.apply(lambda x: x / 100), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Sparkling wines sold and average temperature per month',
                     #y_label='100000 litres of sparkling wine sold and average celcius',
                     a_legend="100000 l of sparkling wine sold", b_legend="Average temperature in " + celsius_string)
#=> 09/2015 big spike? Other than that christmas season and may day seem to be the time of the year with heightened sales

#Graph of Beer sold and average temperature in Finland
create_two_bar_graph(beer[31:].apply(lambda x: x / 100), finland_temp[31:], rain_x_pos, x_tick_labels=graph_months,
                     title='Beer sold and average temperature per month',
                     #y_label='100000 l of Beer sold and average celcius',c=finland_rain[31:].apply(lambda x: x / 10),
                     a_legend="100000 l of beer sold", b_legend="Average temperature in " + celsius_string)

#Graph of red wine sold and average temperature in Finland
create_two_bar_graph(red_wine[31:].apply(lambda x: x / 100), finland_temp[31:], rain_x_pos, x_tick_labels=graph_months,
                     title='Red wines sold and average temperature per month',
                     #y_label='100000 litres of red wine sold and average celcius',c=finland_rain[31:].apply(lambda x: x / 10),
                     a_legend="100000 l of red wine sold", b_legend="Average temperature in " + celsius_string)

#Graph of white wine sold and average temperature in Finland
create_two_bar_graph(white_wine[31:].apply(lambda x: x / 100), finland_temp[31:], rain_x_pos, x_tick_labels=graph_months,
                     title='White wines sold and average temperature per month',
                     #y_label='100000 litres of white wine sold and average celcius',  c=finland_rain[31:].apply(lambda x: x / 10),
                     a_legend="100000 l of white wine sold", b_legend="Average temperature in " + celsius_string)

beer_and_cider=beer
beer_and_cider.add(cider, fill_value=0)

#Graph of beer and ciders sold and average temperature in Finland
create_two_bar_graph(beer_and_cider.apply(lambda x: x / 100), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Beer and cider sold and average temperature per month',
                     #y_label='100000 litres of beer and cider sold and average celcius',
                     a_legend="100000 l of beer and cider sold", b_legend="Average temperature in " + celsius_string)

#Graph of pure alcohol total sold and average temperature in Finland
create_two_bar_graph(pure_alcohol_total.apply(lambda x: x / 100), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='Pure alcohol total sold and average temperature per month',
                     #y_label='100000 litres of pure alcohol total sold and average celcius',
                     a_legend="100000 l of pure alcohol total sold", b_legend="Average temperature in " + celsius_string)

all_wines=red_wine
all_wines=all_wines.add(white_wine,fill_value=0)
all_wines=all_wines.add(sparkling_wine,fill_value=0)
all_wines=all_wines.add(rose_wine,fill_value=0)
all_wines=all_wines.add(other_wine,fill_value=0)

#Graph of all the total of all wines sold and average temperature in Finland
create_two_bar_graph(all_wines.apply(lambda x: x / 1000), finland_temp, x_pos, x_tick_labels=graph_months,
                     title='All wines total sold and average temperature per month',
                     #y_label='1000000 litres of all wines total sold and average celcius',
                     a_legend="1000000 l of all wines total sold", b_legend="Average temperature in " + celsius_string)

#mode, median, better visualization (celcius as a number?), predictions for next year based on old averages
