import os
import requests
import json

headers = {"X-Vault-Token": "s.BRaXUoDzxYxbfBN6Agn5Gzo2"}
url = 'http://127.0.0.1:8200/v1/secret/data/{}'


def export(data):
    for k, v in data.items():
        os.environ[k] = v
    print(os.environ['ENV'])


try:
    ENV = os.environ['ENV']
    if ENV:
        url = url.format(ENV)
        print(url)
        req = requests.get(url, headers=headers)
        data = json.loads(req.text)
        main = data['data']['data']
        export(main)
    else:
        FILE_PATH = os.environ['FILE_PATH']
        with open(FILE_PATH) as json_file:
            data = json.load(json_file)
            main = data['data']['data']
        export(main)
except KeyError:
    raise Exception('either ENV or FILE PATH must be set.')

