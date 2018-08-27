#!/usr/bin/python3

import json
from pprint import pprint

with open('perference.json', 'r') as f:
    data2 = json.load(f)

pprint(data2)
print(data2['man'])
