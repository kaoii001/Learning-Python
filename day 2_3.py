# import re
# m = re.search('(?<=abc)def', 'abcdef')
# print(type(m))
# print(m)

import re 

f = open("D://python/project2/frontend/controllers/Home.php")
x = f.read()

m = re.findall("action[A-Z].*\(.*\)", x)
#print(m)

for elem in m:
    print(re.search("[A-Z][a-z]+", elem).group(0))
    




