import re

a = '1+2+3+55'
list = re.split('\+|\-|\/|\*', a)

print(list)


