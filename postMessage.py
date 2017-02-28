# coding: utf-8
import requests, yaml

config = yaml.load(open("config.yml"))

token = config["access_token"]
channel = config["channel"]
message = config["message"]
url = config["url"]

attachment = '[{"pretext":"' +message+ '","text":"' +url+ '","footer":"Kota: observes then alerts"}]'

postMessage = "https://slack.com/api/chat.postMessage?pretty=true&as_user=false&channel="+channel+"&attachments="+attachment+"&token="+token

requests.get(postMessage)