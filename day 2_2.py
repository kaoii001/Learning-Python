import re 

f = open("D://python/Learning-Python/data/vote.php")
x = f.read()
#print(x)

m = re.findall("function.+\$params\)", x)
#print(m)

func = []
for elem in m:
    print(re.search(" .+\(", elem).group(0)[1:-1])
    func.append(re.search(" .+\(", elem).group(0)[1:-1])