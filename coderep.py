from flask import Flask
from providers import githubResources
from providers import stackoverflowResouces
from database import coderepdb
from settings import APP_STATIC
import json
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'Health_Check!'


@app.route('/github')
def github():
    mockUrl = 'https://api.github.com/repos/django/django'
    check_url = githubResources.check_valid("https://github.com/mbostock/d3")
    stars = githubResources.get_stars(mockUrl)
    return str(stars)


@app.route('/so')
def stackoverflow():
    so = stackoverflowResouces.get_tags('django')
    test = stackoverflowResouces.check_valid("http://api.stackoverflow.com/1.1/tags?filter=abcsdferg")
    return str(so)


@app.route('/savecomp')
def save_component():
    return 'ok'


@app.route('/json')
def generate_json_components():
    components = coderepdb.get_all_components()
    languages = coderepdb.get_all_languages()

    key_name = "name"
    value_name = "components"

    key_children = "children"
    children = []

    key_size = "size"

    array = []

    for language in languages:
        for component in components:
            if language.id == component.language_id:
                comp_dict = {key_name: component.name, key_size: component.rep}
                array.append(comp_dict)

        mutable_dict = {key_name: language.name, key_children: array}
        children.append(mutable_dict)
        array = []

    dict = {key_name: value_name, key_children: children}
    dict = json.dumps(dict, ensure_ascii=False)

    return dict


@app.route('/writefile')
def write_json_file():
    jsonDict = generate_json_components()

    with open(os.path.join(APP_STATIC, 'components.json'), 'w') as f:
        f.write(jsonDict)
        f.close

    return 'ok'


@app.route('/filterbylang/<lang>')
def filter_by_lang(lang):
    with open(os.path.join(APP_STATIC, 'components.json'), 'r') as f:
        dict = json.load(f)
        f.close

    children = []
    dict_lang = None

    array_lang = dict['children']

    for filterLang in array_lang:
        if filterLang['name'] == lang:
            dict_lang = filterLang
            break

    if dict_lang is None:
        return "Error - Not found language with name: " + lang

    children.append(dict_lang)
    json_lang = {"name": "components", "children": children}
    json_lang = json.dumps(json_lang, ensure_ascii=False)

    return json_lang


if __name__ == '__main__':
    app.debug = True
    app.run()