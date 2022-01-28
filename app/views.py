from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    content_news = get_news('content')
    print(content_news)
    title = 'Home - Faska News Channel'
    return render_template('index.html', title = title,popular = content_news)