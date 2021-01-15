import numpy as np

handle = open("D://python/project2/frontend/controllers/Home.php", "r")
data = []

i = 0
while i < 50:
    data.append(handle.readline())
    i = i + 1

i = 0
while i < 50:
    print(str(i) + ">>>" + data[i])
    i = i + 1
handle.close()