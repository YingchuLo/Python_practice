'''
Goa1 1: Remove string in a sentence or
Goal 2: Remove redundant space at the beginning and the end of sentence
'''

import re # regex

def strip_custom(string,x):
    return re.search(' *[{s}]*(.*?)[{s}]* *$'.format(s=x), string).group(1)


print (strip_custom(' aaabtestbcaa ' , 'abc' ))
print(strip_custom('      Hello world.   ' , ' '))

'''
#output
test
Hello world.
'''