# EXAA-volume-prediction
Python script for predicting Austrian electricity Spot prices
I used Aylien News API to gather news and articles relevant to EU energy market - Articles.csv.
The Aylien_news_SDK.py script uses their python SDK(https://docs.aylien.com/newsapi/interactive-documentation) 
to scrape and convert articles to csv file.
Inside dshistory2018.xls are hourly spot prices(and volume) from EXAA for 2018. 

I focused on predicting the daily MWh volume for 1 day ahead, to see if news articles affect(correlate) the future trading movements.

Preprocess_data.py --> The script merges Articles.csv and dshistory2018.xls such that each article represents 1 instance,
meaning that there might be more daily articles predicting same day ahead volume.
The script also transforms(vectorizes) the text making it ready for the learning phase.

For learning and prediction I used sklearn's RandomForestRegressor and R2_score to calculate accuracy.
As expected it performed very badly, since the dataset contains only about 260 articles and the daily volume is 
a big number to predict accurately.
It would be best to start with classification models to only predict increase/decrease in volume relative to day before.

RESULTS:
![Alt text](R2.png?raw=true "Title")
