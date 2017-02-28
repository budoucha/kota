# coding: utf-8

import requests, yaml

config_filename = "config.yml"
config = yaml.load(open(config_filename))

target_url = config["url"]
target_html = requests.get(target_url).text

f=open("ref_html","w")
f.write(target_html)
f.close()