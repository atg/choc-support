#!/usr/bin/env python

import os.path
import os
import json
from StringIO import StringIO
amalg = "{\n\n"

import subprocess

# Run the scripts
print("Generating Python")
subprocess.call("cd python && python modulegen.py", shell=True)

print("Generating Ruby")
subprocess.call("cd ruby && ruby rubyharvest.rb", shell=True)

print("Generating Go")
subprocess.call("cd go && php gogen.php", shell=True)

# 1. Read all the files in languages/
amalgs = []

languages = {}
for d in os.listdir("."):
   if not os.path.isdir(d):
      continue
   if d.startswith("_old"):
      continue
   
   for p in os.listdir(d):
      path = os.path.join(d, p)
      # Get the file's name
      name = os.path.splitext(os.path.basename(path))[0]
      ext = os.path.splitext(os.path.basename(path))[1]
      
      if not ext == '.json': continue
      print(path)
      f = open(path)
      contents = f.read()
      f.close()
      j = json.load(StringIO(contents))
      # 2. Glue them together
      if d in languages:
         languages[d].append(j)
      else:
         languages[d] = [j]
      #amalgs.append('"%s": %s' % (name, contents))

#amalg += ", \n\n".join(amalgs)
#amalg += "\n\n}\n"

# 3. Minify
# amalg = json.dumps(json.load(StringIO(amalg)), separators=(',',':'))
amalg = json.dumps(languages, separators=(',',':'))
#from libraries.json_minify import json_minify

# amalg = json_minify(amalg) + "\n"

f = file("completions.json", "w+")
f.write(amalg)
f.close()
print("Data written to completions.json")

