import aylien_news_api
from aylien_news_api.rest import ApiException
import pprint
import pandas as pd
import datetime


# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'f8351f22'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '1813bb0350110baf87dedd60ca1395ab'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

opts = {
  'text': '"electricity" OR "energy market" OR "energy markets" OR "gas price"',
  #'categories_taxonomy': 'iptc-subjectcode',
  #'categories_id': ["15050004"],
  'sort_by': 'recency',
  'language': ['en'],
  'not_language': ['es', 'it'],
  #'published_at_start': 'NOW-200DAYS',
  #'published_at_end': 'NOW',
  'source_scopes_country' : ['DE',"AT","SI","IT"],
  'per_page' : 100
}

#Get articles containing keywords from "text" parameter. 
#Write them to a .txt file
articles = pd.DataFrame(columns = ["date", "title","body"])

try:
    # List stories
    for i in range(0,19):
      opts['published_at_start'] = 'NOW-' + str(200-10*i) + 'DAYS'
      opts['published_at_end']   = 'NOW-' + str(200-10*(i+1)) + 'DAYS'
      print(200-i*10)
      api_response = api_instance.list_stories(**opts)
      for story in api_response.stories:
        articles.loc[len(articles)] = [datetime.datetime.date(story.published_at), story.title,story.body]
    opts['published_at_start'] = 'NOW-10DAYS'
    opts['published_at_end']   = 'NOW'
    print(10)
    api_response = api_instance.list_stories(**opts)
    for story in api_response.stories:
      articles.loc[len(articles)] = [datetime.datetime.date(story.published_at), story.title,story.body]
    name = input("Please input name of file: ")
    articles.to_csv(name,encoding='UTF8')
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %sn" % e)