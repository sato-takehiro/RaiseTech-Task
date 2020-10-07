import re

path = "wagahaiwa_nekodearu.txt"

# あらかじめ正規表現オブジェクトを作成
pattern = re.compile(r"(《[^《》]*》)|(［[^［］]*］)")

with open(path, encoding="utf-8") as f:
        lines = f.readlines()

count = 0
for l in lines:
        count = count + 1
        l_strip = l.strip()

        match = pattern.finditer(l_strip)
        for m in match:
                print(str(count) + ": " + str(m)) # マッチングオブジェクトをそのまま表示（行番号付き）
                print(m.groups())  # マッチした文字列
                print("GROUP1" + ": " + str(m.group(1))) # 1つ目のグループにマッチした文字列
                print("GROUP2" + ": " + str(m.group(2))) # 2つ目のグループにマッチした文字列
                print("START" + ": " +str(m.start())) # マッチした文字列の先頭位置
                print("END" + ": " +str(m.end())) # マッチした文字列の末尾位置
                print("SPAN" + ": " +str(m.span())) # マッチした文字列の範囲
