from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_Articles,
from .forms import ArticlesForm
from ..models import Articles

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
    title = 'Home - Welcome to The Newshight'
    return render_template('index.html', title = title,sports = sports_sources, entertainment = entertainment_sources, health = health_sources, technology = technology_sources,science = science_sources )

@main.route('/sources/<int:id>')
def sources(id):

    '''
    View news page function that returns the news details page and its data
    '''
    sources = get_sources(id)
    title = f'{sources.title}'

    return render_template('sources.html',title = title,sources = sources)