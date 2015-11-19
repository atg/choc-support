from __future__ import print_function
import json

obsolete = '''
applet
acronym
bgsound
dir
frame
frameset
noframes
hgroup
isindex
listing
nextid
noembed
plaintext
strike
xmp
basefont
big
blink
center
font
marquee
multicol
nobr
spacer
tt
'''
obsolete = set(obsolete.strip().splitlines(False))


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

def main():
  def parse_tags():
    tags = []
    for line in real_lines('html/HTMLTagNames.in'):
      # print(line)
      start, _, end = line.partition(' ')
      ends = end.split(', ')
      ends = [partition_if_in(x, '=') for x in ends]
      ends = dict(ends)
      
      if start in obsolete:
        continue
      if '=' in start:
        continue
      # print(start)
      # print(ends)
      # print()
      
      tags.append(start)
    
    tags = sorted(list(set(tags)))
    return tags
  
  print(json.dumps(parse_tags(), separators=(',',':')))

if __name__ == '__main__':
  main()