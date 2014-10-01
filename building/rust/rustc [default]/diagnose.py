import os
from re import compile as rx
import json
from subprocess import check_output, STDOUT, CalledProcessError

# From flycheck

def build_arguments(root):
    yield "/usr/local/bin/rustc"
    yield "--no-trans"
    yield "--color"
    yield "never"
    
    if root:
        yield "--crate-type"
        yield ('bin' if is_executable_project(root) else 'lib')
        
        yield "-L"
        yield os.path.join(root, 'target')
        yield os.path.join(root, 'target', 'deps')
    
    yield os.environ['CHOC_FILE']
    
def is_executable_project(root):
    #   (or (string= "src/main.rs" rel-name)
    #       (string-prefix-p "src/bin/" rel-name)))
    return (
        os.path.exists(os.path.join(root, 'src', 'main.rs'))
        or os.path.exists(os.path.join(root, 'src', 'bin'))
    )

def project_root():
    root = os.environ.get('CHOC_PROJECT_DIR')
    if os.path.exists(os.path.join(root, 'cargo.toml')) or os.path.exists(os.path.join(root, 'Cargo.toml')):
        return root
    return None

def invoke():
    output = ''
    try:
        output = check_output(list(build_arguments(project_root())), stderr=STDOUT)
    except CalledProcessError as e:
        output = e.output
    # output = str(commands.getoutput("""$SHELL -cl 'rustc --no-trans --color never "$CHOC_FILE"'"""))
    parse(output)

ERROR_RE = rx(r':(\d+):(\d+): \d+:\d+ (error|warning|info): ([^\n]+)')

def parse(output):
    matches = ERROR_RE.findall(output)
    display(map(parse_match, matches))

def parse_match(match):
    # path = match[0]
    line = int(match[0])
    column = int(match[1])
    err_type = match[2]
    message = match[3]

    return {
        'path': '',
        'line': line,
        'message': message.replace('`', "'"),
        'column': column,
        'type': err_type,
    }

def display(output):
    print json.dumps(output)

invoke()
