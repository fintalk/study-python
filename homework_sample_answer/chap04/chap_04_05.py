# P168の replace()メソッドの例を写経して実行して下さい
# pass 

# P168の 文字列の削除と数値への変換を写経して実行して下さい
# pass 

# replace メソッドを使ってバナナをりんごに変更して下さい
text = "I love banana."
text = text.replace("banana", "apple")
print(text)


text = "AA A B C DDD A C D"
text = text.replace("A", "B")
print(text)

text = "AA A B C DDD A C D"
text = text.replace("A", "")
print(text)

s = "$125,040"
s = int(s.replace(",","").replace("$", ""))
print(s)
