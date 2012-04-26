import sys, os, re, collections, pprint, json

header = """// I needed a list of the most popular HTML tags so I could tweak Chocolat's (http://chocolatapp.com) code completion.
// The tags were gathered from the top 1000 websites.
// Note: The parser is fairly simple and has no comprehension of <style> or <script> elements, which is why there are some strange, non-html tags (such as "<n", from for loops I assume).


"""
import math

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

#sys.exit(0)

allcontent = [ open('topsitehtml/' + name, 'r').read() for name in os.listdir('topsitehtml') ]

tallied = { }
tags = []
for content in allcontent:
    contenttallied = dict(tally([x.lower() for x in re.findall('<([a-zA-Z]+)[\s>]', content)]))
    
    contenttallied = { k: logorzero(contenttallied[k]) for k in contenttallied }
    
    for k in contenttallied:
       if k not in tallied:
           tallied[k] = 0.0
       tallied[k] += contenttallied[k]
    
    # total = float(sum(contenttallied.values()))
    # ratios = { k: float(contenttallied[k]) / total for k in contenttallied }
    
    #for k in ratios:
    #    if k not in tallied:
    #        tallied[k] = []
    #    tallied[k].append(ratios[k])
    
    # tags.extend()

# for k in tallied.copy():
#     print k
#     tallied[k] = geomean(tallied[k]) * 100.0

import operator
tallied = sorted(tallied.iteritems(), key=operator.itemgetter(1), reverse=True)

#tallied = tally(tags).most_common()



print pprint.pprint(tallied)

# import operator
# x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
# sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))

print header + '{\n  ' + ',\n  '.join('%s: %f' % (repr(name), count) for name, count in tallied) + '\n}'

# print json.dumps(tally(tags), indent=2)
# print pprint.pprint(tally(tags))
