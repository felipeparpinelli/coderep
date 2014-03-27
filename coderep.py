from flask import Flask
from providers import githubResources
from providers import stackoverflowResouces

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'Health_Check!'


@app.route('/github')
def github():
    mockUrl = 'https://api.github.com/repos/django/django'
    stars = githubResources.getStars(mockUrl)
    return str(stars)


@app.route('/so')
def stackoverflow():
    so = stackoverflowResouces.getTags('django')
    return str(so)


@app.route('/savecomp')
def saveComponent():
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run()