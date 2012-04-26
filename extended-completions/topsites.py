import csv, pprint, json, re, urllib2

f = open("topsites.txt", "r")
reader = csv.reader(f, delimiter="\t")

for row in reader:
    site = row[1].strip()
    print site
    try:
        content = urllib2.urlopen('http://www.' + site).read()
    except:
        try:
            content = urllib2.urlopen('http://' + site).read()
        except Exception as e:
            print '  ' + repr(e)
            continue
    open('topsitehtml/' + site, 'w').write(content)
