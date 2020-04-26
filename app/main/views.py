from flask import render_template,request
from . import main
from ..requests import get_sources_by_cat,get_all_articles,get_headline_articles
from ..models import Source,Article

# Changing app routes to main route
# Views
# @app.route('/')
# def index():

@main.route('/')
def general():

    '''
    View root page function that returns the news sources
    '''
    general = get_sources_by_cat('general')
    business = get_sources_by_cat('business')
    sports = get_sources_by_cat('sports')
    technology = get_sources_by_cat('technology')
    science = get_sources_by_cat('science')
    health = get_sources_by_cat('health')
    entertainment = get_sources_by_cat('entertainment')
    
    title = 'News Now'
    return render_template('general.html',title=title,general=general,business = business,sports = sports,technology = technology,health=health,science=science,entertainment = entertainment)

@main.route('/articles/<id>')
def articles(id):
    '''
    view page function that returns the source articles
    '''
    articles = get_all_articles(id)
    title = 'News Now'


    return render_template('articles.html', articles=articles, title=title)


@main.route('/headlines/<en>')
def headlines(en):
    '''
    view page function that returns the topheadlines by langauge
    '''
    headlines = get_headline_articles('en')
    title = 'News Now'


    return render_template('headlines.html', headlines=headlines, title=title)

    
  
