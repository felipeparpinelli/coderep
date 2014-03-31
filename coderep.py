from flask import Flask
from providers import githubResources
from providers import stackoverflowResouces
from database import coderepdb

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


@app.route('/json')
def generateJsonComponents():
    components = coderepdb.getAllComponents()
    languages = coderepdb.getAllLanguages()

    keyName = "name"
    valueName = "components"

    keyChildren = "children"
    valueChildren = []

    keySize = "size"

    array = []

    for language in languages:
        for component in components:
            if language.id == component.language_id:
                compDict = {keyName: component.name, keySize: component.rep}
                array.append(compDict)

        mutableDict = {keyName: language.name, keyChildren: array}
        valueChildren.append(mutableDict)
        array = []

    dict = {keyName: valueName, keyChildren: valueChildren}
    print(dict)

    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run()