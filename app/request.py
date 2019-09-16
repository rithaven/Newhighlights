import urllib.request,json
from .models import sources,Articles
from datetime import datetime

# Getting api key
api_key = None
# Getting the News base url
base_url = None
#getting the Articles url
Articles_url = None

def configure_request(app):
    global api_key,base_url, Articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_API_BASE_URL']
    Articles_url = app.config['ARTICLES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''
    sources_results = []

    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

       
        sources_object = sources(id,name,description,url,category,language,country)
        sources_results.append(sources_object)


    return sources_results

def get_Articles(id):
    '''
    Function that process the articles and returns a list of articles objects
    '''
    get_Articles_url = Articles_url.format(id,api_key)

    with urllib.request.urlopen(get_Articles_url) as url:
           Articles_results = json.loads(url.read())

           Articles_object = None
           
           if Articles_results['articles']:
               Articles_object = process_Articles(Articles_results['articles'])
    
    return Articles_object

def process_Articles(Articles_list):
    
    Articles_object = []

    for Articles_item in Articles_list:
              id = Articles_item.get('id')
              name = Articles_item.get('name')
              author = Articles_item.get('author')
              title = Articles_item.get('title')
              url = Articles_item.get('url')
              urlToImage = Articles_item.get('urlToImage')
              publishedAt = Articles_item.get('publishedAt')
              content = Articles_item.get('content')

              if urlToImage:
                  Articles_results = Articles(id,name,author,title,url,urlToImage,publishedAt,content)
                  Articles_object.append(Articles_results)


    return Articles_object

        