import re

path = "wagahaiwa_nekodearu.txt"

# あらかじめ正規表現オブジェクトを作成
pattern = re.compile(r"《[^《》]*》|［[^［］]*］")

with open(path, encoding="utf-8") as f:
        lines = f.readlines()

count = 0
for l in lines:
        count = count + 1
        l_strip = l.strip()

        match = pattern.findall(l_strip)
        if(len(match)):
                for w in range(len(match)):
                        print(str(count) + "行 " + str(w) + "個目：" + str(match[w]))
