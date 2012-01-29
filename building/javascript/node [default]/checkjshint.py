import commands
import re
import json

def invoke():
    output = str(commands.getoutput("sh env/jsc.sh $CHOC_FILE \"laxbreak:true,laxcomma:true\""))
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
    return {
        'path': '',
        'line': line,
        'message': message,
        'column': column,
        'type': 'error',
    }

def display(output):
    print json.dumps(output)

invoke()
