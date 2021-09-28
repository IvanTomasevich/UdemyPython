import re

file = open("sample.txt", encoding="utf-8")

info = file.read()

file.close()

print(info)

# print(re.match(r"abcdefghijklmnopqrstuvwxyz", info))
print(re.findall(r"\+\d-[-\(\d\)]+", info))
