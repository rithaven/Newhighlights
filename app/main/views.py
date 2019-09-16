from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_Articles
from ..models import sources

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting  general news
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')
    technology_sources = get_sources('technology')
    science_sources = get_sources('science')
    title = ' Welcome to The News highlight'
    return render_template('index.html', title = title,sports = sports_sources, entertainment = entertainment_sources, health = health_sources, technology = technology_sources,science = science_sources )

@main.route('/sources/<id>')
def Articles(id):

    '''
    View news page function that returns the news articles details page and its data
    '''
    Articles = get_Articles(id)
    title = f'search result for {id}'

    return render_template('Articles.html',title = title,Articles = Articles)