import json
import os
import re

# https://github.com/msanders/snipmate.vim/tree/master/snippets

def process(lines):
    items = []
    for line in lines:
        line = line.rstrip()
        if not line:
            continue
        
        if line[0] == '[':
            header_lang, header_tab = re.findall(r'\[\^?([^\]\s]+) ([^\]]+)\]', line)[0]
            
            items.append({
                'keyEquiv': None,
                'content': '',
                'tabTrigger': header_tab,
                'language': header_lang,
                'scopeSelector': None,
                'type': 'snippet',
                'name': header_tab,
                'anchorStart': line[1] == '^',
            })
        else:
            items[-1]['content'] += line + '\n'
    
    for item in items:
        s = item['content']
        s = s.replace('    ', '\t')
        s = s.replace('  ', '\t')
        s = re.sub(r'\{(\d+)', r'%{\1', item['content'])
        s = s.rstrip()
        item['content'] = s
    
    return items

def main():
    items = os.listdir('langs')
    out_items = []
    for item in items:
        if item.endswith('.txt'):
            with open('langs/' + item, 'rb') as f:
                lines = list(f)
                out_items.extend(process(lines))
    
    with open('default_snippets.json', 'wb') as f:
        json.dump({ 'items': out_items }, f)

if __name__ == '__main__':
    main()

