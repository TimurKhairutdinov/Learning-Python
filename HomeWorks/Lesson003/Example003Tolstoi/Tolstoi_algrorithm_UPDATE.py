from collections import Counter
import json

text = ''
with open('tolstoi.txt', 'r', encoding='utf-8') as data:
    for line in data:
        text += ' ' + line.lower() 
        print(f'text + done {line}')
    print('Open complete!')

ls = text.split()

with open('result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(Counter(ls), ensure_ascii=False))
    print('result complete!')


