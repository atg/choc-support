import commands
import re
import json

def invoke():
    print commands.getoutput('echo hello')
    
    output = str(commands.getoutput("bash pyflakes.sh $CHOC_SOURCE_FILE"))
    parse(output)

def parse(output):
    print output
    errormessage = r'^([^:\n]+):(\d+): ([^\n]+)'
    caretposition = r'( *)\^ *'
    fullregex_inner = r'%s(\n[^\n]+\n%s)?' % (errormessage, caretposition)
    fullregex = re.compile(fullregex_inner, re.MULTILINE)
    matches = re.findall(fullregex, output)
    display(map(parse_match, matches))

def parse_match(match):
    path = match[0]
    line = int(match[1])
    message = match[2]
    caret_outer = match[3]
    caret_inner = match[4]
    
    column_index = -1
    if len(caret_outer) > 0:
        column_index = len(caret_inner)
    
    return {
        'path': path,
        'line': line,
        'message': message,
        'column_index': column_index,
        'type': 'error',
    }

def display(output):
    print json.dumps(output)

invoke()