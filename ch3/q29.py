import json
import urllib.parse
import urllib.request

with open('q28.json', 'r') as f:
    dct = json.load(f)

lst = [dct['国旗画像'], dct['位置画像']]

url = 'https://www.mediawiki.org/w/api.php?'

for l in lst:
    params = {
        'action' : 'query',
        'titles' : 'File:' + l,
        'prop' : 'imageinfo',
        'iiprop' : 'url',
        'format' : 'json'
    }

    paramstr = urllib.parse.urlencode(params)
    req = urllib.request.Request(url + paramstr)
    with urllib.request.urlopen(req) as res:
        dct = json.loads(res.read().decode('utf8'))
        print(dct['query']['pages']['-1']['imageinfo'][0]['url'])