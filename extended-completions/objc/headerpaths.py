import re
import os, sys
import json
import sqlite

##### Regexes from objcfix #####

def flatten(listOfLists):
    return chain.from_iterable(listOfLists)

def ident(x):
    return x.replace('IDENT', '[a-zA-Z_][a-zA-Z0-9_]*')

def parsemeth(methgroup):
    return ' '.join(methgroup.rstrip().split())

def selector_from_signature(sig):
    sig = sig.lstrip()

    comps = re.findall(sig_re, sig)
    if not comps:
        comps = [re.findall(basic_sig_re, sig)[-1]]
    return (sig[0]) + ''.join(comps)

def make_sane_whitespace(s):
    return ' '.join(s.split())


# @interface regex
interface_re = re.compile(ident(r'@interface\s+(IDENT)\s*(\:\s*(IDENT)(<(IDENT)>)?|\(\s*(IDENT)\s*\)|\(\))([\s\S]+?)@end(\b|$)'), re.MULTILINE) # Do people really define their own base classes?

# @implementation regex
implementation_re = re.compile(ident(r'@implementation\s+(IDENT)\s*((\(\s*(IDENT)\s*\)|\(\))?)([\s\S]+?)@end(\b|$)'), re.MULTILINE)

# #import/#include regex
import_re = re.compile(r'\s*#\s*(import|include)\s*["<]([^">\n]+)[">]', re.MULTILINE)

# @class regex
class_re = re.compile(ident(r'@class\s*((IDENT)(\s*,\s*IDENT)*)\s*;'), re.MULTILINE)

# Method definition/declaration regex
method_re = r'^\s*([+\-][a-zA-Z0-9&$:()^*\[\]<>\s]+)'
method_def_re = re.compile(method_re + r'\{', re.MULTILINE)
method_dec_re = re.compile(method_re + r';', re.MULTILINE)

# Message send regex
message_re = re.compile(r'...', re.MULTILINE)

# Signature regex

# - (void) foo :a bar:b baz:c ;
sig_re = re.compile(ident(r'IDENT\:'))
# - (void) foo ;
basic_sig_re = re.compile(ident(r'(IDENT)\s*$'))



ios_root = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.1.sdk/System/Library/Frameworks'
j = {
    'items': [],
    'prototypes': [],
}
frameworks = ['Foundation', 'AppKit', 'CoreData', 'QuartzCore', 'QTKit', 'WebKit']
ios_frameworks = ['UIKit', 'Twitter', 'EventKit']

def findallin(rootroot):
    for frameworkdir in os.listdir(rootroot):
        try:
            #for framework in frameworks:
            frameworkroot = os.path.join(rootroot, '%s/Headers' % frameworkdir) # '/System/Library/Frameworks/%s.framework/Headers' % framework
            for headername in os.listdir(frameworkroot):
                headerpath = os.path.join(frameworkroot, headername)
                with open(headerpath, 'r') as f:
                    s = f.read()
                    for iface in interface_re.findall(s):
                        name = iface[0]
                        body = iface[6]
                        for method in method_dec_re.findall(body):
                            method = method.strip()
                            classinstancesymbol = method[0]
                            isinstancemethod = (classinstancesymbol == '-')
                            #print '%s[%s %s]' % (classinstancesymbol, name, selector_from_signature(method)[1:])
                            #print '  ' + make_sane_whitespace(method)
                            j['items'].append(selector_from_signature(method)[1:])
                            j['prototypes'].append(make_sane_whitespace(method))
                        #sys.exit()
        except:
            pass



findallin('/System/Library/Frameworks')
findallin(ios_root)

j['items'] = sorted(list(set(j['items'])))
j['prototypes'] = sorted(list(set(j['prototypes'])))

print json.dumps(j, separators=(',',':'))


# need:
## last_insert_id()
## query(q, [params])
## macclasses{class name -> { "methods" -> set() }}
# method_to_prototype{ class_method_name -> prototype }

initsqls = """CREATE TABLE classes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, exists_ios INT, exists_mac INT)
CREATE INDEX classes_index ON classes (name COLLATE NOCASE)
CREATE TABLE methods (id INTEGER PRIMARY KEY AUTOINCREMENT, selector TEXT, class_id INT, is_class_method INT, prototype_id INT, exists_ios INT, exists_mac INT)
CREATE INDEX methods_index ON methods (selector COLLATE NOCASE)
CREATE TABLE symbols (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, prototype_id INT, exists_ios INT, exists_mac INT)
CREATE INDEX symbols_index ON symbols (name COLLATE NOCASE)
CREATE TABLE prototypes (id INTEGER PRIMARY KEY AUTOINCREMENT, prototype TEXT)"""

for initsqlquery in initsqls:
    query(initsqlquery, [])

# Create classes
classmap = {}
for cl in set(macclasses.keys()) | set(iosclasses.keys()):
    query("INSERT INTO classes (name, exists_ios, exists_mac) VALUES (?, ?, ?)", [
        cl,
        int(cl in iosclasses),
        int(cl in macclasses),
    ])
    classmap[cl] = last_insert_id()
    
    # Create methods
    macmethods = macclasses[cl]['methods'] if cl in macclasses else set()
    iosmethods = iosclasses[cl]['methods'] if cl in iosclasses else set()
    for method in macmethods | iosclasses:
        
        query("INSERT INTO prototypes (prototype) VALUES (?)", [
           method_to_prototype[cl + ' ' + method]
        ])
        
        prototype_id = last_insert_id()
        
        query("INSERT INTO methods (selector, class_id, is_class_method, prototype_id, exists_ios, exists_mac) VALUES (?, ?, ?, ?, ?, ?)", [
            method[1:],
            classmap[cl],
            (1 if method[0] == '+' else '-'),
            prototype_id,
            int(cl in iosmethods),
            int(cl in macmethods),
        ])
        
        

