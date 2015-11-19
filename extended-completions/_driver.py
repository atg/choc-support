import subprocess
import json

j = subprocess.check_output(['/usr/bin/env', 'python', 'html/parse.py'])
j = json.loads(j)
print(j)
