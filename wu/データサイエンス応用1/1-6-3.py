path = "wagahaiwa_nekodearu.txt"

with open(path, encoding="utf-8") as f:
        lines = f.readlines()

count = 0
for l in lines:
        count = count + 1
        print(str(count) + ": " + l)

