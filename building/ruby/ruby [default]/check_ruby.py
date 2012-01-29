import commands
import re
import json

def invoke():
    output = str(commands.getoutput("ruby -c $CHOC_FILE"))
    parse(output)

# PHP Parse error:  syntax error, unexpected T_PAAMAYIM_NEKUDOTAYIM in test.php on line 3
# Errors parsing test.php

def parse(output):
    errormessage = r'^([^\n:]+):(\d+):\s+([^\n]+)'
    fullregex = re.compile(errormessage, re.MULTILINE)
    matches = re.findall(fullregex, output)
    display(map(parse_match, matches))

def parse_match(match):
    # path = match[0]
    line = int(match[1])
    message = match[2]
    
    return {
        'path': '',
        'line': line,
        'message': message,
        'column': -1,
        'type': 'warning' if 'warning' in message else 'error',
    }

def display(output):
    print json.dumps(output)

invoke()
