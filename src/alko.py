import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alkosales.csv")

#Invert and assing all columns to a variable for easy access
month = df['Month'].iloc[::-1]
vodka_spirit = df['VodkaAndSpirit'].iloc[::-1]
other_spirit = df['OtherSpirit'].iloc[::-1]
fortified_wine = df['FortifiedWine'].iloc[::-1]
red_wine = df['RedWine'].iloc[::-1]
white_wine = df['WhiteWine'].iloc[::-1]
sparkling_wine = df['SparklingWine'].iloc[::-1]
rose_wine = df['RoseWine'].iloc[::-1]
other_wine = df['OtherWine'].iloc[::-1]
cider = df['Cider'].iloc[::-1]
long_drink = df['LongDrink'].iloc[::-1]
beer = df['Beer'].iloc[::-1]
non_alcoholic_beverage = df['NonAlcoholicBeverage'].iloc[::-1]
total = df['Total'].iloc[::-1]
pure_alcohol_total = df['PureAlcoholTotal'].iloc[::-1]

print(month)
print(vodka_spirit)

#Plot vodka sales per month
graph_months = (month.apply(lambda x: x[:2]))
y_pos = np.arange(len(graph_months))

plt.bar(y_pos, vodka_spirit, align='center', alpha=0.5)
plt.xticks(y_pos, graph_months)
plt.ylabel('1000 litres of vodka and spirits sold')
plt.xlabel('Month')
plt.title('Vodka and spirit sales in ton litres per month')

plt.show()
