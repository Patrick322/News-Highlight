from app import app
import urllib.request,json
form .trends import news

News = news.news


# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request