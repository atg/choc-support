#!/usr/bin/env python

import os.path
import os

amalg = "{\n\n"

# 1. Read all the files in languages/
amalgs = []

for path in os.listdir("languages"):
   # Get the file's name
   name = os.path.splitext(os.path.basename(path))[0]
   f = open(os.path.join("languages", path))
   contents = f.read()
   f.close()
   
   # 2. Glue them together
   amalgs.append('"%s": %s' % (name, contents))

amalg += ", \n\n".join(amalgs)
amalg += "\n\n}\n"


# 3. Minify

from libraries.json_minify import json_minify

amalg = json_minify(amalg) + "\n"

f = file("data.json", "w+")
f.write(amalg)
f.close()
print("Data written to data.json")