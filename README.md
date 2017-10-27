Alko's monthly sales and weather in Finland
======


## The research idea
We are trying to find out if there is any correlation between weather, holidays and Alko’s alcohol sales. If such a correlation exists we will try to predict next years sales.


## Predictions
We think it is likely that certain types of beverage sales are seasonal, meaning that weather will have an impact on the sales. Also it seems likely that the consumption of cheaper alcohols e.g. beers doesn’t vary a lot because of external conditions. 


## Analysis and data
Our data set is from Alko’s public monthly sales data from 03/2013 to 09/2017 and from Finnish Meteorological Institution’s open source weather data. 
A problem presented itself as Alko’s sales data was given only on a monthly basis. It would have been more useful if we had had data on the daily sales or at least on the weekly sales. Then we would have been able to achieve more accurate results. This would have made it possible for us to isolate the effect of seasonal holidays like New year's eve and First of May on Alko’s sales. 
We found collecting weather data somewhat challenging because weather data was not uniformly available for all places in Finland. We gathered our weather data from four different cities that had enough data available and that were in different parts of Finland. This made it possible to calculate the approximate average weather for each month in Finland.


## The work
The data was gathered from excel files and visual representations (plots) and parsed into csv files. The csv files were read into pandas dataframes and plotted out with mathlibplot. Finding a good way to visualize the data took suprisingly long time because there were so many moving parts that made the graphs rather confusing to read. 


![overall](/images/overall.png)


On this graph we have plotted the average temperature in Finland and overall sales from Alko and the average amount of rain from 03/2013 to 09/2017. There is definately some seasonal changes in the sales. This might point to a correlation between temperature and the sales.


![overall with rain](/images/withRain.png)


This is the same graph as above but now from 09/2015 to 09/2017, as we didn't find good rain data for the years before that. We can see that amount of rain doesn't affect Alko's sales at all.


![rose wine](/images/rose.png)


Rose wines are good example where the monthly sales are strongly correlated with the monthly temperature. Interestingly the sales increase steadily from 2013 to 2017 which might be due to improved selections in rose wines in Alko. 


![sparkling wine](/images/sparkling.png)


Sparkling wines best show the effect of seasonal holidays on sales. May day and New Years Eve standout strongly from rest of the graph in April and December. There is also correlation between the temperature and sales. Maybe people like to celebrate their holidays with some sparkling wine?


![vodka and spirits](/images/vodka.png)


Some beverages like strong alcohols are not affected as heavily by the changing of seasons. Again we can see the effect of New Years on the sales but other than that the changes are not very strong. Still we can see somekind of pattern here with the rising temperature.


## Results
Overall there is seems to be a correlation between overall sales and weather. For some beverages the effects are very obvious and for some the sales are almost constant. During certain seasonal holidays (Christmas, New Years, May day, Midsummer day) Alko’s sales are strongly heightened. In summer there are more sales done than during other seasons. This is most likely caused by the increased temperature and/or the summer vacation season.


## Prospects
These results might be useful to corporations that own bars, pubs or restaurants. They could use their sales data and weather forecasts to predict approximately how much beverage sales they are going to have in the future. This information could be used to create discounts for products that are going to sell poorly or to pick the correct “throw-in” products for the night. Also having data on sales beforehand would make it easier to have everything in stock.
