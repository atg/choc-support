import re
import json

# See: http://peter.sh/experiments/vendor-prefixed-css-property-overview/

s = open('peter.sh experiments vendor-prefixed-css-property-overview.txt', 'r').read()

r = re.compile('-?[a-z][a-z\-]+[a-z]')
a = re.findall(r, s)
a = list(sorted(set(a)))

prefixes = ['-apple', '-wap', '-epub', '-xv']
a = [x for x in a if not any([
    x.startswith(prefix) for prefix in prefixes
])]

def dict_for_property(prop):
    
    # ADD PROPERTY SPECIFIC STUFF HERE
    vals = []
    if '-color' in prop:
        vals.append("<color>")
    return { "values": vals }

j = { prop: dict_for_property(prop) for prop in a }

#print '\n'.join(a)

f = open('css3-original.do-not-edit-by-hand.json', 'w+')
f.write(json.dumps(j))
f.close()

