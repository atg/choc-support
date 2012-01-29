import commands
import re
import json

def invoke():
    output = str(commands.getoutput("php -l $CHOC_FILE"))
    parse(output)

# PHP Parse error:  syntax error, unexpected T_PAAMAYIM_NEKUDOTAYIM in test.php on line 3
# Errors parsing test.php

def parse(output):
    errormessage = r'^[^\n]+error:\s+([^\n]+) in ([^\n]+) on line (\d+)'
    fullregex = re.compile(errormessage, re.MULTILINE)
    matches = re.findall(fullregex, output)
    display(map(parse_match, matches))

def parse_match(match):
    path = match[1]
    line = int(match[2])
    message = match[0]
    
    return {
        'path': path,
        'line': line,
        'message': message,
        'column': -1,
        'type': 'warning' if 'warning' in message else 'error',
    }

def display(output):
    print json.dumps(output)

invoke()
