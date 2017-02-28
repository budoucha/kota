# coding: utf-8

import requests, yaml
from time import sleep

config_filename = "config.yml"
config = yaml.load(open(config_filename))
sleepTime = float(config["sleepTime"])

target_url = config["url"]
target_html = requests.get(target_url).text

f = open("ref_html","r")

if target_html != f.read():
    ktkr=open("ktkr","w")
    brk=open("break","w")
    ktkr.close()
    brk.close()

f.close()

sleep(sleepTime)