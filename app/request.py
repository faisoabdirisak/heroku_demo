from app import app
import urllib.request,json
from app.models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# GEtting the news base url
base_url = app.config["NEWS_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results 


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for new_item in news_list:
        title = new_item.get('title')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content= new_item.get('content')

        if title:
            news_object = News(title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results    