import math
import sys, os, re, collections, pprint, json

header = """// I needed a list of the most popular HTML tags so I could tweak Chocolat's (http://chocolatapp.com) code completion.
// The tags were gathered from the top 1000 websites.
// Note: The parser is fairly simple and has no comprehension of <style> or <script> elements, which is why there are some strange, non-html tags (such as "<n", from for loops I assume).


"""

def tally(xs):
    cnt = collections.Counter()
    for x in xs:
        cnt[x] += 1
    return cnt

def geomean(xs):
    print xs
    prod = reduce(lambda x, y: x * y, sorted(xs, reverse=True))
    return pow(prod, 1.0 / len(xs))

def logorzero(n):
    return math.log(n + 1)

allcontent = [ open('topsitehtml/' + name, 'r').read() for name in os.listdir('topsitehtml') ]

tallied = { }
tags = []

TAGS_RE = '<([a-zA-Z]+)[\s>]'
ATTR_RE = ' ([a-zA-Z]+)=["\']'

for content in allcontent:
    contenttallied = dict(tally([x.lower() for x in re.findall(ATTR_RE, content)]))
    contenttallied = { k: logorzero(contenttallied[k]) for k in contenttallied }
    
    for k in contenttallied:
       if k not in tallied:
           tallied[k] = 0.0
       tallied[k] += contenttallied[k]

import operator
tallied = sorted(tallied.iteritems(), key=operator.itemgetter(1), reverse=True)

print pprint.pprint(tallied)

print header + '{\n  ' + ',\n  '.join('%s: %f' % (repr(name), count) for name, count in tallied) + '\n}'
