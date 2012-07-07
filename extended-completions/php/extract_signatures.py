import os
import re
import HTMLParser
import json

TAGS_RE = re.compile(r'</?[a-zA-Z][^>]*>')
WHITESPACE_RE = re.compile(r'\s+')

def striptags(s):
    return HTMLParser.HTMLParser().unescape(
        WHITESPACE_RE.sub(' ', TAGS_RE.sub('', s).replace('\n', ' '))
    )


j = {
    "items": [],
    "prototypes": [],
    "icon":"function",
    "extendedConfidence": True,
}
r = "php-chunked-xhtml"
for n in os.listdir(r):
    if not n.startswith('function.'):
        continue
    p = os.path.join(r, n)
    with open(p, 'r') as f:
        s = f.read()
        # <div class="methodsynopsis dc-description">
        if '<div class="methodsynopsis dc-description">' not in s:
            continue
        
        sig = striptags(re.findall(r'<div class="methodsynopsis dc-description">([\s\S]+?)</div>', s)[0])
        
        fname = re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', sig)[0]
        #print fname
        j['items'].append(fname)
        j['prototypes'].append(sig)
        
        #print sig

print json.dumps(j, separators=(',', ':'))
