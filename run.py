# coding: utf-8

import requests
import json
import sys
from api_key import API_KEY
import pprint

args = sys.argv

sentence = args[1]
sensitivity = "medium"

sensitivity_tuple = ("low", "medium", "high")

if args[2:3] and args[2] in sensitivity_tuple:
    sensitivity = args[2]

url = 'https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo?apikey={apikey}&sentence={sentence}&sensitivity={sensitivity}'.format(
    apikey=API_KEY, sentence=sentence, sensitivity=sensitivity)
responce = requests.get(url)

data = json.loads(responce.text)

pprint.pprint(data)
