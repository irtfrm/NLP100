import gzip
import json

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        dct = json.loads(line)
        if dct['title'] == 'イギリス':
            with open('jawiki-uk.txt', 'w') as uk:
                uk.write(dct['text'])
            break