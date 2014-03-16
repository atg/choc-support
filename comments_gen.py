from pprint import pprint

def comments_gen():
    with open('comments.txt', 'rb') as f:
        current_group = None
        for line in f:
            is_data = line.startswith(' ')
            line = line.strip()
            
            if not line:
                continue
            
            if is_data:
                items = line.split()
                if len(items) == 1:
                    # Line comment
                    current_group['line_comments'].append(items[0])
                else:
                    # Block comment
                    current_group['block_comments'].append(items)
            else:
                if current_group:
                    yield current_group
                
                current_group = {
                    'languages': line.split(),
                    'line_comments': [],
                    'block_comments': [],
                }
        
        if current_group:
            yield current_group

def escape(s):
    return s.replace('\\', '\\\\').replace('"', r'\"')

def matcher(lang):
    return 'MATCH_LANG(@"%s")' % lang

def comments_header():
    is_first = True
    for group in comments_gen():
        matchers = ' || '.join(map(matcher, group['languages']))
        
        if is_first:
            yield 'if (%s) {' % matchers
        else:
            yield 'else if (%s) {' % matchers
        
        is_first = False
        
        for lc in group['line_comments']:
            yield '    MATCH_LINE_COMMENT(@"%s");' % escape(lc)
        for bcs, bce in group['block_comments']:
            yield '    MATCH_BLOCK_COMMENT(@"%s", @"%s");' % (escape(bcs), escape(bce))
        
        yield '}'
            
    #pprint(list(comments_gen()))

def main():
    with open('comments.h', 'wb') as f:
        for line in comments_header():
            f.write(line + '\n')

if __name__ == '__main__':
    main()