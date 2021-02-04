s1 = "we love python"
s2 = "ABCDEFGABCDEFG"
name1 = "Smitty Swarbrick"
name2 = "Roxanna Eskrigg"
address1 = "1 Chome-4-1 Kabukicho, Shinjuku City, Tokyo 160-8484"
address2 = "〒163-8001 東京都 新宿区 西新宿二丁目 8番 1号"

# address1 から tokyo という単語を探して下さい
print(address1.find("tokyo"))
# address1 から osaka という単語を探して、ValueErrorを出して下さい。
# print(address1.index("osaka"))

# s1 に ruby という単語があるかどうかBooleanで返して下さい。（Booleanで返す、とは True もしくは False で値を得ることです。真偽値で返すともいいます）
print("ruby" in s1)
print(s1.find("ruby") > 0) 

# name1 が Swarbrick で始まっているかBooleanで返して下さい
print(name1.startswith("Swarbrick"))

# name1 が 前から数えて７番目で、Sw で始まっているかBooleanで返して下さい
print(name1.startswith("Sw", 7))

# address1 を ['1', 'Chome-4-1', 'Kabukicho,', 'Shinjuku', 'City,', 'Tokyo', '160-8484'] というリストに変換してください
print(address1.split(" "))

# s2 を "D" で分割し、['ABC', 'EFGABC', 'EFG']というリストに変換してください
print(s2.split("D"))

# s1 を "we love ruby" に変換して下さい
print(s1.replace("python", "ruby"))

# address2 からスペースを取り除いて下さい
print(address2.replace(" ", ""))

# name2を全て大文字にしてください
print(name2.upper())

# name2を全て小文字にしてください
print(name2.lower())

# s2 を ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'] というリストに変換して 変数 l1 に代入して下さい
l1 = list()
for s in s2:
    l1.append(s)
print(l1)

# 実はこれだけでもOK
# print(list(s2))

# l1 を s2 に戻してください。
print("".join(l1))
