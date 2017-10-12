import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patche as mpatches

df = pd.read_csv("alkosales.csv")

#Assing all columns to a variable for easy access
month = df['Month']
vodka_spirit = df['VodkaAndSpirit']
other_spirit = df['OtherSpirit']
fortified_wine = df['FortifiedWine']
red_wine = df['RedWhine']
white_wine = df['WhiteWhine']
sparkling_wine = df['SparklingWhine']
rose_wine = df['RoseWhine']
other_wine = df['OtherWine']
cider = df['Cider']
long_drink = df['LongDrink']
beer = df['Beer']
non_alcoholic_beverage = df['NonAlcoholicBeverage']
total = df['Total']
pure_alcohol_total = df['PureAlcoholTotal']


