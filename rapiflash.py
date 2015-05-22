import urllib2
import json
url = "http://api.devinmui.c9.io/api/v1"
def all():
    response = urllib2.urlopen(url + "/floods")
    data = json.loads(response.read())
    return data
def find(id):
    response = urllib2.urlopen(url + "/floods/" + str(id))
    data = json.loads(response.read())
    return data
    