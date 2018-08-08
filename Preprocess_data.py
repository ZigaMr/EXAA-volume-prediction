import pandas as pd
import datetime
from sklearn.feature_selection.text import CountVectorizer

#Komentar na datum 8.8.2018dsadasdsdsasdads
articles = pd.read_csv(r'Articles.csv')
volumes  = pd.read_excel(r'dshistory2018.xls',sheet_name='Volume (MWh)')


articles = articles.drop(['Unnamed:0'],axis = 1)
articles.index = pd.to_datetime(articles.date)
articles = articles.drop(['date'],axis=1)
volumes = volumes.iloc[1:,[-1]]
volumes.index = pd.to_datetime(volumes.index)
volumes = volumes.rename(index = str,columns = {'Unnamed: 24': "vol"})
vol = list(volumes.vol[:-1])
volumes = volumes.iloc[1:]
volumes.vol = vol

#Vectorize the body text from articles
skupni = volumes.join(articles).dropna()
#Change the index because the date won't be used as a feature
skupni.index = [i for i in range(len(skupni))]
a = CountVectorizer()
b = a.fit_transform(skupni)
count_vect_df = pd.DataFrame(b.todense(), columns=a.get_feature_names())

skupni = pd.concat([skupni,count_vect_df],axis=1).drop(['title','body','date'],axis=
X  = skupni.drop(["vol"],axis=1)
Y  = skupni.vol
