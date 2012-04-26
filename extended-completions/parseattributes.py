import csv, pprint, json, re

# http://www.whatwg.org/specs/web-apps/current-work/multipage/section-index.html#attributes-1

isminified = True

d = open("attributes.tsv", "r")
d2 = open("tags.tsv", "r")
reader = csv.reader(d, delimiter="\t")
reader2 = csv.reader(d2, delimiter="\t")

tophtml = json.loads(open("tophtmltags.json", "r").read())
tophtmlattrs = json.loads(open("tophtmlattributes.json", "r").read())

tags = {}
for row in reader:
    # print row
    valuedescription = row[3].strip()
    attrvalues = []
    if 'oolean attribute' in valuedescription:
        attrvalues.append(row[0].strip())
    attrvalues.extend(re.findall(r'"([^"]*)"', valuedescription))
    # print row[3].strip()
    # print '  ' + repr(attrvalues)
    
    attrtags = [s.strip() for s in row[1].split(";")]
    for attrtag in attrtags:
        if attrtag == 'HTML elements':
            attrtag = "<all>"
        if attrtag not in tags:
            tags[attrtag] = {
                # "name": attrtag.strip(),
                "attributes": {},
            }
        
        tags[attrtag]['attributes'][row[0].strip()] = {
            "name": row[0].strip(),
            "description": row[2].strip(),
            "value-description": valuedescription,
            "values": attrvalues,
        }

for row in reader2:
    
    names = [s.strip() for s in row[0].split(",")]
    for name in names:
        if name not in tags:
            tags[name] = {
                # "name": name
            }
    
        tags[name]['description'] = row[1].strip()
        tags[name]['categories'] = [s.strip() for s in row[2].split(';')]
        tags[name]['parents'] = [s.strip() for s in row[3].split(';')]
        tags[name]['children'] = [s.strip() for s in row[4].split(';')]
        tags[name]['interface'] = row[6].strip()
    
    # print row


empty_tags = []
block_tags = []
inline_tags = []
unknown_tags = []

snippets = {
    "a": '<a href="%{1}">%{0}</a>',
    
    "audio": '<audio src="%{1}">%{0}</audio>',
    
    "canvas": '<canvas id="%{1}" width="%{2}" height="%{3}">%{0}</canvas>',
    
    "embed": '<embed type="%{1}" src="%{2}">',
    
    "iframe": '<iframe src="%{1}">%{0}</iframe>',
    
    "input": '<input name="%{1}" type="%{0="text"}">',
    
    "div": '<div class="%{1}">\n\t%{0}\n</div>',
    
    "span": '<span class="%{1}">%{0}</span>',
    
    "label": '<label for="%{1}">%{0}</label>',
    
    "source": '<source src="%{0}">',

    "link": '<link href="%{1}" rel="%{2="stylesheet"}" type="%{3="text/css"}">',
    
    # ol
    "ol": '''<ol>
\t<li>%{0}</li>
</ol>''',
    
    # ul
    "ul": '''<ul>
\t<li>%{0}</li>
</ul>''',
    
    # select
    "select": '''<select>
\t<option>%{0}</option>
</select>''',
    
    # table
    "table": '''<table>
\t<tr>%{0}</tr>
</table>''',
    
    # style
    "style": '''<style>

%{0}

</style>''',
    
    
    # form
    "form": '''<form action="%{1}" method="%{2="post"}" accept-charset="utf-8">
\t%{0}
\t<p><input type="submit" value="Next"></p>
</form>''',
    
    # head
    "head": '''<head>
\t<meta charset="utf-8">
\t<title>%{1}</title>
\t
\t<link href="style.css" rel="stylesheet" type="text/css">
\t
</head>''',
    
    # body
    "body": '''<body>
\t
\t%{0}
\t
</body>''',
    
    # html
    "html": '''<html>
<head>
\t<meta charset="utf-8">
\t<title>%{1}</title>
\t
\t<link href="style.css" rel="stylesheet" type="text/css">
\t
</head>
<body>
\t
\t%{0}
\t
</body>
</html>''',
    
}


for t in sorted(list(tags)):
    if t in tophtml:
        tags[t]['popularity'] = tophtml[t]
    else:
        tags[t]['popularity'] = 0.0
    
    if 'attributes' not in tags[t]:
        tags[t]['attributes'] = { }
    
    for a in list(tags[t]['attributes']):
        attrdict = tags[t]['attributes'][a]
        if a in tophtmlattrs:
            attrdict['popularity'] = tophtmlattrs[a]
        else:
            attrdict['popularity'] = 0.0
    
    if 'children' in tags[t]:
        # print t
        ch = tags[t]['children']
        if t not in ['li', 'th', 'blockquote', 'td', 'caption'] and ('flow' in ch or 'flow*' in ch or t in ['colgroup', 'hgroup', 'html', 'head', 'body', 'ol', 'ul', 'dl', 'style', 'select', 'optgroup', 'script', 'table', 'tbody', 'tfoot', 'thead', 'tr', 'th', 'div', 'datalist']):
            block_tags.append(t)
            tags[t]['kind'] = 'block'
        elif 'empty' in ch:
            empty_tags.append(t)
            tags[t]['kind'] = 'empty'
        elif 'phrasing' in ch or 'phrasing*' in ch or 'transparent*' in ch or 'transparent' in ch or t in ['iframe', 'noscript', 'textarea', 'option', 'title', 'td', 'th', 'blockquote', 'li', 'caption']:
            inline_tags.append(t)
            tags[t]['kind'] = 'inline'
        else:
            # print t
            # print '  ' + ', '.join(ch)
            
            unknown_tags.append(t)
            tags[t]['kind'] = 'inline'
    
    if t in snippets:
        tags[t]['snippet'] = snippets[t]

#print empty_tags
#print block_tags
#print inline_tags
#print ''
#print unknown_tags

# pprint.pprint(tags)
if isminified:
    print json.dumps(tags, sort_keys=True)
else:
    print json.dumps(tags, sort_keys=True, indent=4)


# print repr({ t: { 'snippet': '' } for t in sorted(list(tags)) })

