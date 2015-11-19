from __future__ import print_function
import csv, pprint, json, re

def partition_if_in(xs, x):
  if x in xs:
    a, _, b = xs.partition(x)
    return (a, b)
  else:
    return (xs, '')
  
def real_lines(path):
  with open(path, 'r') as f:
    for line in f:
      line = line.strip()
      if line.startswith('//'):
        continue
      if '//' in line:
        line, _, _ = line.partition('//')
      line = line.strip()
      if not line:
        continue
      yield line



isminified = False

def uniq(inpt):
    output = []
    for x in inpt:
        if x not in output:
            output.append(x)
    return output

class Properties(object):
  def __init__(self):
    self.data = {}
  
  def read_original(self):
    original_f = open("css-original.json", "r")
    
    self.concat(json.load(original_f))
    
  def add_bare(self, xs):
    for x in xs:
      if x in self.data: continue
      self.data[x] = { "values": [] }
  
  def concat(self, d):
    for k, v in d.items()[:]:
      for sk in k.split(' '):
        if sk in self.data: continue
        self.data[sk] = v.copy()
  
  def map_recursive_values(self):
    recursive_values = ['background-attachment', 'background-color', 'background-image', 'background-position', 'background-repeat', 'cue-after', 'cue-before', 'font-family', 'font-size', 'font-style', 'font-weight', 'font-weight', 'line-height', 'list-style-image', 'list-style-position', 'list-style-type', 'outline-color', 'outline-style', 'outline-width']
    
    d = self.data
    for k in d:
      for v in d[k]['values'][:]:
        if v in recursive_values:
          d[k]['values'].extend(d[v]['values'])
          d[k]['values'].remove(v)
        try:
          if int(v, 10) < 50:
            d[k]['values'].remove(v)
        except:
          pass
    
        d[k]['values'] = uniq(d[k]['values'])
    
  
  def prefix_merge_values(self):
    # Add color
    for k, v in self.data.items():
      vals = v['values']
      if '<color>' not in vals:
        if '-color' in k or k == 'color':
          vals.append("<color>")
    
    # Merge prefixed into normal
    prefixes = ['-webkit-', '-moz-', '-o-', '-ms-', '-apple-']
    for k in self.data:
      for prefix in prefixes:
        if k.startswith(prefix):
          unprefixed = k[len(prefix):]
          if unprefixed not in self.data:
            continue
          leftvals = self.data[k]['values']
          rightvals = self.data[unprefixed]['values']
          rightvals = sorted(list(set(leftvals) | set(rightvals)))
          self.data[k]['values'] = rightvals
    
    # Merge normal into prefixed
    for k in self.data:
      for prefix in prefixes:
        if k.startswith(prefix):
          unprefixed = k[len(prefix):]
          if unprefixed not in self.data:
            continue
          leftvals = self.data[unprefixed]['values']
          rightvals = self.data[k]['values']
          rightvals = sorted(list(set(leftvals) | set(rightvals)))
          self.data[unprefixed]['values'] = rightvals
  
  def mark_top(self):
    topcss = json.loads(open("csstop.json", "r").read())
    for k in self.data:
      p = 0.0
      if k in topcss:
        p = topcss[k]
      
      self.data[k]['popularity'] = p


def compile_all():
  isminified = True
  
  topcss = json.loads(open("csstop.json", "r").read())
  original_f = open("css-original.json", "r")
  fcss3 = open("css3-original.do-not-edit-by-hand.json", "r")
  
  d = json.loads(fcss3.read())
  # Prefer original ones to css3 ones
  d.update(json.loads(original_f.read()))
  
  recursive_values = ['background-attachment', 'background-color', 'background-image', 'background-position', 'background-repeat', 'cue-after', 'cue-before', 'font-family', 'font-size', 'font-style', 'font-weight', 'font-weight', 'line-height', 'list-style-image', 'list-style-position', 'list-style-type', 'outline-color', 'outline-style', 'outline-width']
  
  allvals = set()
  allkeys = set()
  for k in d:
    for v in d[k]['values'][:]:
      if v in recursive_values:
        d[k]['values'].extend(d[v]['values'])
        d[k]['values'].remove(v)
      try:
        if int(v, 10) < 50:
          d[k]['values'].remove(v)
      except:
        pass
  
      d[k]['values'] = uniq(d[k]['values'])
  
  for k in d.copy():
      d2 = d[k]
      del d[k]
      for k2 in k.split():
          d[k2] = d2
  
  for k in list(d):
      p = 0.0
      if k in topcss:
          p = topcss[k]
  
      d[k]['popularity'] = p

def main():
  def parse_petersh():
    props = []
    for line in real_lines('css/peter.sh2015'):
      if line:
        props.extend(x for x in line.split())
    return props
  
  def parse_properties():
    props = []
    for line in real_lines('css/CSSProperties.in'):
      start, _, end = line.partition(' ')
      ends = end.split(', ')
      ends = [partition_if_in(x, '=') for x in ends]
      ends = dict(ends)
      
      if 'svg' in ends:
        continue # ignore svg for now
      if 'alias_for' in ends:
        props.append(ends['alias_for'])
      if start.startswith('-epub-'):
        continue # ignore epub
      props.append(start)
    return props
  
  def parse_values():
    # Would be easier to get these from MDN
    with open('css/CSSValueKeywords.in', 'r') as f:
      for line in f:
        pass
        # CSSValueKeywords is almost useless
        "font-weigth" # real typo in there!
  
  
  
  
  # parse_values()
  props = parse_properties()
  props.extend(parse_petersh())
  
  props = sorted(list(set(props)))
  
  p = Properties()
  p.read_original() # must be done first!
  p.add_bare(props)
  p.map_recursive_values()
  p.prefix_merge_values()
  p.mark_top()
  pprint.pprint(p.data)
  with open('css.min.json', 'w') as f:
    json.dump(p.data, f, separators=(',',':'))

if __name__ == '__main__':
  main()