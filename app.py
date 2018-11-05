from flask import Flask,render_template,flash,request,url_for
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#bootstrap=Bootstrap(app)

#默认flask 路由
#-------------------------------------
#@app.route('/')
#def hello_world():
#    return 'Hello World!'
#---------------------------------------


user = {
    'username':'Grey Li',
    'bio':'A boy who loves movies and music.',
}
movies = [
     {'name':'My Neighboor Totoro','year':'1988'},
     {'name': 'Three Colours trilogy', 'year': '1993'},
     {'name': 'Forrest Gump', 'year': '1994'},
     {'name': 'Prefect Blue', 'year': '1997'},
     {'name': 'The Matrix', 'year': '1999'},
     {'name': 'Memento', 'year': '2000'},
     {'name': 'The Bucket list', 'year': '2007'},
     {'name': 'Black Swan', 'year': '2010'},
     {'name': 'Gone Girl', 'year': '2014'},
     {'name': 'CoCo', 'year': '2017'},
]

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies=movies)

@app.route('/')
def index():
    return render_template('index.html')

@app.context_processor
def inject_foo():
    foo = 'i an foo.'
    return dict(foo=foo)

@app.template_global()
def bar():
    return 'I am bar.'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')

if __name__ == '__main__':
    app.run()
