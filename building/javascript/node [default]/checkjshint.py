import commands
import re
import json

def invoke():
    true_options = [
        "laxcomma",
        "laxbreak",
        "eqnull",
        
        "es5",
        "esnext",
        "iterator",
        "multistr",
        "scripturl",
        "smarttabs",
        "supernew",

        "asi",
    ]
    
    options_arg = ','.join([opt + ':true' for opt in true_options])
    #print "sh env/jsc.sh $CHOC_FILE \"%s\"" % options_arg
    output = str(commands.getoutput("sh env/jsc.sh $CHOC_FILE \"%s\"" % options_arg))
    parse(output)

def parse(output):
    errormessage = r'^(.+)\(line: (\d+), character: (\d+)'
    fullregex = re.compile(errormessage, re.MULTILINE)
    matches = re.findall(fullregex, output)
    display(map(parse_match, matches))

def parse_match(match):
    line = int(match[1])
    message = match[0]
    column = match[2]
    
    t = 'warning'
    if 'Expected' in message or 'Unmatched' in message:
        t = 'error'
    if 'Expected a conditional expression and instead saw an assignment' in message:
        t = 'warning'
    t
    return {
        'path': '',
        'line': line,
        'message': message,
        'column': column,
        'type': t,
    }

def display(output):
    print json.dumps(output)

invoke()
