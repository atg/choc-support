import csv, pprint, json, re

isminified = False

def uniq(inpt):
    output = []
    for x in inpt:
        if x not in output:
            output.append(x)
    return output

isminified = True

topcss = json.loads(open("csstop.json", "r").read())

f = open("css-original.json", "r")
fcss3 = open("css3-original.do-not-edit-by-hand.json", "r")

d = json.loads(fcss3.read())
# Prefer original ones to css3 ones
d.update(json.loads(f.read()))



recursive_values = ['background-attachment', 'background-color', 'background-image', 'background-position', 'background-repeat', 'cue-after', 'cue-before', 'font-family', 'font-size', 'font-style', 'font-weight', 'font-weight', 'line-height', 'list-style-image', 'list-style-position', 'list-style-type', 'outline-color', 'outline-style', 'outline-width']

allvals = set()
allkeys = set()
for k in d:
    # print d[k]['values']
    for v in d[k]['values'][:]:
        if v in recursive_values:
            d[k]['values'].extend(d[v]['values'])
            d[k]['values'].remove(v)
        try:
            if int(v, 10) < 50:
                d[k]['values'].remove(v)
        except:
            pass
    
    d[k]['values'] = uniq(d[k]['values'])

for k in d.copy():
    d2 = d[k]
    del d[k]
    for k2 in k.split():
        d[k2] = d2

for k in list(d):
    p = 0.0
    if k in topcss:
        p = topcss[k]
    
    d[k]['popularity'] = p


# for k in d:
#     allkeys.add(k)
#     print k
#     for v in d[k]['values']:
#         print '  ' + v
#         allvals.add(v)
#     print ''

# keyvals = allvals & allkeys
# allvals = set()
# for k in d:
#     for v in d[k]['values']:
#         allvals.add(v)
# for v in sorted(list(allvals)):
#    print v


if isminified:
    print json.dumps(d, sort_keys=True)
else:
    print json.dumps(d, sort_keys=True, indent=4)

