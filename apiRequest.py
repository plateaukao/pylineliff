# -*- coding: utf-8 -*-
import requests
from os.path import join, dirname
import dotenv
import json

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

LIFF_BASE_URL = "https://api.line.me/liff/v1/apps"
LIFF_ACCESS_TOKEN_KEY = "LIFF_ACCESS_TOKEN"


def default_headers():
    headers = {"Authorization": "Bearer " + dotenv.get_key(dotenv_path, LIFF_ACCESS_TOKEN_KEY),
               "Content-Type": "application/json"}
    return headers


def liff_init(access_token):
    dotenv.set_key(dotenv_path, LIFF_ACCESS_TOKEN_KEY, access_token)


def liff_add(url, size_type):
    data = {"view": {"type": size_type, "url": url}}
    response = requests.post(LIFF_BASE_URL, headers=default_headers(), json=data)
    response_json_dic = json.loads(response.text)
    return response_json_dic


def liff_delete(liff_id):
    return requests.delete(LIFF_BASE_URL + "/" + liff_id, headers=default_headers())


def liff_update(liff_id, view):
    return requests.put(LIFF_BASE_URL + "/" + liff_id + "/view", headers=default_headers(), json=view)


def liff_list():
    response = requests.get(LIFF_BASE_URL, headers=default_headers())
    response_json_dic = json.loads(response.text)
    return response_json_dic


