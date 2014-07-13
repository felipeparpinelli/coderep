from flask import Flask, render_template, jsonify
from providers import github_resources
from providers import stackoverflow_resouces
from database import coderepdb
from models import component
from models import language
import urllib
import json
from flask import request
import history
from models import pending_component

app = Flask(__name__)

comp = None
array_langs = None

@app.route('/health_check')
def health_check():
    return 'Health_Check!'


def update_rep():
    components = coderepdb.get_all_components()

    for component in components:
        tags = component.tags
        stars = component.stars

        new_rep = tags + stars

        if new_rep is not None and component.rep is not None:
            component.rep = new_rep
            coderepdb.update_values(component)
    return 'ok'


@app.route('/filterbylang/<lang>', methods=['GET'])
def filter_by_lang(lang):
    global comp
    if comp is None:
        comp = component.generate_json_components()
    dict = json.loads(comp)

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
    ret = {"name": "components", "children": children}
    ret2 = json.loads(history.filter_by_lang(lang))
    j = []
    j.append(ret)
    j.append(ret2)
    return jsonify(result=j)


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/python', methods=['GET'])
def python():
    ret = {"msg": "Select a language", "error": 1}
    return jsonify(ret), 200


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/getcomps', methods=['GET'])
def get_comps():
    global comp
    comp = component.generate_json_components()
    return comp


@app.route('/gethistory', methods=['GET'])
def get_history():
    _history = history.create_json_history()
    return _history


@app.route('/getlanghistory', methods=['GET'])
def get_lang_history():
    _history = history.create_json_lang_history()
    return _history


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/languages', methods=['GET'])
def lang():
    return render_template('language.html')


@app.route('/submit', methods=['POST'])
def submit():

    data = request.data
    data = data.split('&')
    component_name = data[0].split('=')
    component_name = component_name[1]
    github_url = data[1].split('=')
    github_url = github_url[1]
    github_url = urllib.unquote(github_url).decode('utf8')
    lang = data[2].split('=')
    lang = lang[1]
    lang_id = data[3].split('=')
    lang_id = lang_id[1]
    is_gh_valid = True
    is_so_valid = True

    if coderepdb.exist_component(component_name, github_url):
        ret = {"msg": "That component already exists", "error": 1}
        return jsonify(ret), 200

    if component_name is '' and str(github_url) is '':
        ret = {"msg": "Fill in at least one field", "error": 1}
        return jsonify(ret), 200

    if lang_id is str(0):
        ret = {"msg": "Select a language", "error": 1}
        return jsonify(ret), 200

    if not github_resources.check_valid(github_url) and github_url != '':
        ret = {"msg": "Please, enter a valid github url", "error": 1}
        return jsonify(ret), 200

    git_repo_name = github_resources.get_repo_name(github_url)

    github_url_api = github_url.replace("https://github.com/", "https://api.github.com/repos/")
    github_stars = github_resources.get_stars(github_url_api)
    if github_stars is 'error':
        is_gh_valid = False

    if stackoverflow_resouces.get_tags(component_name) is 0:
        is_so_valid = False

    if is_so_valid is False and is_gh_valid is False:
        ret = {"msg": "No information found for " + component_name + ' ' + github_url, "error": 1}
        return jsonify(ret), 200

    if not coderepdb.get_language_id(lang) and lang_id == str(-1):
        ret = {"msg": "Unfortunately we didn't find the " + lang + " language in our database. A request to add it was sent.", "error": 1}
        return jsonify(ret), 200

    if git_repo_name == component_name and lang == github_resources.lang:
        _comp = create_component(component_name, github_stars, github_url, lang)
        ret = {"msg": "OK! Registered successfully.", "error": 0}
        history.set_new_comp(_comp, lang)
        coderepdb.insert_component(_comp)
    else:
        pendingComp = create_pending_comp(component_name, github_stars, github_url, lang)
        ret = {"msg": "OK! Pending approval.", "error": 0}
        coderepdb.insert_component(pendingComp)

    return jsonify(ret), 200


def create_component(component_name, github_stars, github_url, lang):
    _comp = component.Component(str(component_name), int(github_stars), int(stackoverflow_resouces.get_tags(component_name)),
                                        int(int(github_stars) + int(int(stackoverflow_resouces.get_tags(component_name)))),
                                        str(github_url), int(coderepdb.get_language_id(lang)))
    _comp.name = str(component_name)
    _comp.github_url = str(github_url)
    _comp.stars = int(github_stars)
    _comp.tags = int(stackoverflow_resouces.get_tags(component_name))
    _comp.rep = int(float(_comp.stars) + float(_comp.tags))
    _comp.language_id = int(coderepdb.get_language_id(lang))
    print coderepdb.get_language_id(lang)

    return _comp

def create_pending_comp(component_name, github_stars, github_url, lang):
    _comp = pending_component.PendingComponent(str(component_name), int(github_stars), int(stackoverflow_resouces.get_tags(component_name)),
                                        int(int(github_stars) + int(int(stackoverflow_resouces.get_tags(component_name)))),
                                        str(github_url), int(coderepdb.get_language_id(lang)))
    _comp.name = str(component_name)
    _comp.github_url = str(github_url)
    _comp.stars = int(github_stars)
    _comp.tags = int(stackoverflow_resouces.get_tags(component_name))
    _comp.rep = int(float(_comp.stars) + float(_comp.tags))
    _comp.language_id = int(coderepdb.get_language_id(lang))

    return _comp


@app.route('/searchlangs', methods=['GET'])
def search_langs():
    global array_langs
    key = '/lang/' + history.get_date_sys()
    value = history.get_history(key)
    if value is None or array_langs is None:
        history.set_lang_history()
        array_langs = language.generate_json_languages()

    return array_langs


if __name__ == '__main__':
    app.debug = True
    app.run()