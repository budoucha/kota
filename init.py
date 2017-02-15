# coding: utf-8

import requests

target_url = open("config.txt").read()

target_html = requests.get(target_url).text

f=open("html","w")

f.write(target_html)

f.close()