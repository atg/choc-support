import re

constants = {
    'icon': 'constant',
    'prototypes': [],
    'items': [],
    'extendedConfidence': True,
}

functions = {
    'icon': 'function',
    'prototypes': [],
    'items': [],
    'extendedConfidence': True,
}

methods = {
    'icon': 'method',
    'prototypes': [],
    'items': [],
    'extendedConfidence': True,
    'scope': 'file',
}

with open('allfunctions.txt') as f:
    for line in f:
        line = line.replace('\xc2\xb7\xc2\xb7\xc2\xb7', '...').rstrip()
        xs = methods
        n = re.findall(r'[\.a-zA-Z0-9]+\:([\.a-zA-Z0-9]+)\s*\(', line)
        if not n:
            xs = functions
            n = re.findall(r'([\.a-zA-Z0-9]+)\s*\(', line)
            if not n:
                xs = constants
                n = re.findall(r'([\.a-zA-Z0-9]+)\s*$', line)
        
        n = n[0]
        xs['items'].append(n)
        xs['prototypes'].append(line)

import json, pprint
pprint.pprint(methods)
#print json.dumps(functions)

def outputasjson(n, j):
    with open(n + '.json', 'w+') as f:
        f.write(json.dumps(functions, sort_keys=True, indent=4))

outputasjson('functions', functions)
outputasjson('constants', constants)
outputasjson('methods', methods)

