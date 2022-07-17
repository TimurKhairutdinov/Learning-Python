from os import remove


i = 0
while i < 29648:
    with open(f'file{i}.py', 'a', encoding='utf-8') as fh:
        del fh
        
