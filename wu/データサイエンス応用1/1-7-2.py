import re

path = "wagahaiwa_nekodearu.txt"

with open(path, encoding="utf-8") as f:
        lines = f.readlines()

count = 0
for l in lines:
        count = count + 1
        l_strip = l.strip()

        match = re.findall(r"《[^《》]*》", l_strip)
        #match = re.findall(r"［[^［］]*］", l_strip)
        #match = re.findall(r"《[^《》]*》|［[^［］]*］", l_strip)

        if(len(match) > 0):
           print(str(count) + ": " + str(match))
