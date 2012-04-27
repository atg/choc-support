import sys, os, re, collections, pprint, json, urllib2, hashlib

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
tallied = { }
tags = []

TAGS_RE = '<([a-zA-Z]+)[\s>]'
ATTR_RE = ' ([a-zA-Z]+)=["\']'

def ununi(s):
    return "".join(x if ord(x) < 128 else '' for x in s)

styles = {}
for name in os.listdir('topsitecss'):
    f = open('topsitecss/' + name, 'r')
    content = f.read()
    f.close()
    
    # Check if this is html
    if '<html>' in content or '<body>' in content or '<title>' in content or '<div>' in content or '<a>' in content:
        continue
    
    allpn = []
    for prop in re.findall(r'(?<=[;{\s])([a-z\-]+)\:([^\n;{}:]+);', content):
        propname = prop[0].strip()
        propvalue = prop[1].strip()
        if propname in ['http', 'https', 'javascript', 'ftp', 'mailto'] or len(propvalue) > 60 or len(propname) > 20 or len(propname) < 3:
            continue
        
        pn = ununi(propname)
        if len(pn) != len(propname):
            continue
        
        pv = ununi(propvalue)
        if len(pv) != len(propvalue):
            continue
        
        # if propname not in styles:
        #             styles[pn] = [pv]
        #         else:
        #             styles[pn].append(pv)
        #         
        allpn.append(pn)
        if not isinstance(pn, basestring):
            print pn
        
    contenttallied = dict(tally(allpn))
    contenttallied = { k: logorzero(contenttallied[k]) for k in contenttallied }
    
    for k in contenttallied:
       if k not in tallied:
           tallied[k] = 0.0
       tallied[k] += contenttallied[k]
        
        # print (propname, propvalue)

import operator
tallied = sorted(tallied.iteritems(), key=operator.itemgetter(1), reverse=True)
#pprint.pprint(tallied)
print header + '{\n  ' + ',\n  '.join('%s: %f' % (repr(name), count) for name, count in tallied) + '\n}'

#ff = open('topcsskv.json', 'w')
#ff.write(json.dumps(styles))
#ff.close()

"""
urls = []
for name in os.listdir('topsitehtml'):
    f = open('topsitehtml/' + name, 'r')
    content = f.read()
    f.close()
    for link in re.findall('<link ([^>]+)>', content):
        if '.css' in link:
            #print link
            ms = re.findall(r'''(?:http[^\n"'\s]+%s)?[^\n"'\s]+\.css[^\n"'\s]*''' % name, link)
            if len(ms) != 1:
                continue
            url = ms[0].strip()
            if not url:
                continue
            if not url.startswith('http'):
                if not url.startswith('/'):
                    url = '/' + url
                url = 'http://www.' + name + url
            
            urls.append(url)
            # https://www.paypalobjects.com/WEBSCR-640-20120331-1/css/core/global.css
print len(urls)

for site in urls:
    print site
    try:
        content = urllib2.urlopen(site, timeout=1).read()
    except Exception as e:
        print '  ' + repr(e)
        continue
    if len(content):
        # print content
        sitehash = hashlib.md5(site).hexdigest()[:60]
        print sitehash
        f = open('topsitecss/' + sitehash, 'w')
        f.write(content)
        f.close()
        
    else:
        print '  null content'
"""
# for content in allcontent:
#     contenttallied = dict(tally([x.lower() for x in re.findall(ATTR_RE, content)]))
#     
#     contenttallied = { k: logorzero(contenttallied[k]) for k in contenttallied }
#     
#     for k in contenttallied:
#        if k not in tallied:
#            tallied[k] = 0.0
#        tallied[k] += contenttallied[k]

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

#import operator
#tallied = sorted(tallied.iteritems(), key=operator.itemgetter(1), reverse=True)

#tallied = tally(tags).most_common()



#print pprint.pprint(tallied)

# import operator
# x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
# sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))

#print header + '{\n  ' + ',\n  '.join('%s: %f' % (repr(name), count) for name, count in tallied) + '\n}'

# print json.dumps(tally(tags), indent=2)
# print pprint.pprint(tally(tags))
