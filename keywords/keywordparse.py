import json

with open("keywords.txt", "r") as f:
    lastkey = None
    keywordsmap = {}
    for line in f:
        line = line.strip()
        if not line: continue
        if line == '???': continue
        if line.startswith('['):
            lastkey = line.strip('[]')
        else:
            keywordsmap[lastkey] = line.split()
    
    print '''
    static NSDictionary* CHLanguageKeywords() {
        static dispatch_once_t once;
        static NSDictionary* allkeywords;
        dispatch_once(&once, ^{
            allkeywords = %s;
        });
    }
    ''' % json.dumps(keywordsmap, indent=4, separators=(',', ': ')).replace('{', '@{').replace('[', '@[').replace(' "', ' @"').replace('{"', '{@"').replace('["', '[@"')

    