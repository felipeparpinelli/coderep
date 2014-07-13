__author__ = 'Felipe'

import datetime
import string
import redis
import settings
from models import component, language
import json


r = redis.StrictRedis(host=settings.REDIS_URI, port=6379, db=0)


def get_date_sys():
    date = str(datetime.date.today())
    date = string.replace(date, "-", "")
    return date


def set_history():
    key = get_date_sys()
    json_components = component.generate_json_components()
    r.set(key, json_components)


def set_lang_history():
    key = '/lang/' + get_date_sys()
    json_lang = language.generate_json_languages()
    r.set(key, json_lang)


def get_history(key):
    return r.get(key)


def get_all_history():
    keys = r.keys('*')
    for key in keys:
        print r.get(key)


def create_json_history():

    array = []

    keys = r.keys('*')

    for key in keys:
        if "/" not in key:
            dict = {"date": key}
            data = json.loads(r.get(key))
            lang_length = len(data["children"])
            i = 0
            while i < lang_length:
                j = 0
                comp = len(data["children"][i]["children"])
                while j < comp:
                    comp_name = data["children"][i]["children"][j]["name"]
                    comp_name = str(comp_name)
                    comp_size = data["children"][i]["children"][j]["size"]
                    if 200000 > comp_size > 5000:
                        comp_size = str(comp_size)
                        dict[comp_name] = comp_size
                    j += 1
                i += 1
            array.append(dict)

    array = json.dumps(array, ensure_ascii=False)

    return array


def create_json_lang_history():

    array = []

    keys = r.keys('*')

    for key in keys:
        if "/" in key:
            data = json.loads(r.get(key))
            key = key.replace('/lang/', '')
            dict = {"date": key}
            i = 0
            while i < len(data[0]):
                comp_name = data[0][i]
                comp_name = str(comp_name)
                comp_size = data[1][i]
                comp_size = str(comp_size)
                dict[comp_name] = comp_size
                i += 1
            array.append(dict)

    j_array = json.dumps(array, ensure_ascii=False)

    return j_array


def filter_by_lang(lang):

    array = []

    keys = r.keys('*')

    for key in keys:
        if "/" not in key:
            dict = {"date": key}
            data = json.loads(r.get(key))
            lang_length = len(data["children"])
            i = 0
            while i < lang_length:
                j = 0
                comp = len(data["children"][i]["children"])
                while j < comp:
                    if data["children"][i]["name"] == lang:
                        comp_name = data["children"][i]["children"][j]["name"]
                        comp_name = str(comp_name)
                        comp_size = data["children"][i]["children"][j]["size"]
                        comp_size = str(comp_size)
                        dict[comp_name] = comp_size
                    j += 1
                i += 1
            array.append(dict)

    array = json.dumps(array, ensure_ascii=False)

    return array


def set_new_comp(comp, lang):

    keys = r.keys('*')

    for key in keys:
        data = json.loads(r.get(key))
        lang_length = len(data["children"])
        i = 0
        while i < lang_length:
            if data["children"][i]["name"] == lang:
                data["children"][i]["children"].append({"name": comp.name, "size": comp.rep})
            i += 1
        json_components = json.dumps(data)
        r.set(key, json_components)
    return 'ok'
