# -*- coding: utf-8 -*-
import requests
from os.path import join, dirname
import dotenv
import json
import sys

dotenv_path = join(dirname(__file__), '.env')
# The open behavior is a little different in py2 and py3
# Using 'w+' always truncate the file to 0 length in py3 
if sys.version_info[0] == 2:
    file = open(dotenv_path, 'w+')
else:
    file = open(dotenv_path, 'a')

dotenv.load_dotenv(dotenv_path)

LIFF_BASE_URL = "https://api.line.me/liff/v1/apps"
LIFF_ACCESS_TOKEN_KEY = "LIFF_ACCESS_TOKEN"


def default_headers():
    access_token = dotenv.get_key(dotenv_path, LIFF_ACCESS_TOKEN_KEY)
    if access_token == None:
        print("please call liff.py init first <accessToken>")
        sys.exit()
    headers = {"Authorization": "Bearer " + access_token,
               "Content-Type": "application/json"}
    return headers


def liff_init(access_token):
    if not dotenv.set_key(dotenv_path, LIFF_ACCESS_TOKEN_KEY, access_token):
        print("Cannot save the token to local")


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


