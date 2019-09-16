import os

class Config:

    NEWS_SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&{}apiKey={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&{}apiKey{}'
    
    NEWS_API_KEY = os.environ.get('ddff26e502374e02aca82141982a349d')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}