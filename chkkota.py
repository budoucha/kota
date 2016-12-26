# coding: utf-8

import requests

target_url = open("config.txt").read()

target_html = requests.get(target_url).text

f=open("html","r")

if target_html!=f.read():
    ktkr=open("ktkr","w")
    brk=open("break","w")
	ktkr.close()
    brk.close()

f.close()