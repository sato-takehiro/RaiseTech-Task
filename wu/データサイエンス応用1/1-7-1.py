import re

path = "wagahaiwa_nekodearu.txt"

# あらかじめ正規表現オブジェクトを作成
pattern = re.compile(r"《[^《》]*》")
#pattern = re.compile(r"［[^［］]*］")
#pattern = re.compile(r"《[^《》]*》|［[^［］]*］")

with open(path, encoding="utf-8") as f:
        lines = f.readlines()

count = 0
for l in lines:
        count = count + 1
        l_strip = l.strip()

        match = pattern.findall(l_strip)

        if(len(match) > 0):
           print(str(count) + ": " + str(match))

