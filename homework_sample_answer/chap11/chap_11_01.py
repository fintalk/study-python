# P350 の urillibモジュールの機能を使う、を写経して実行してください
pass 

# P351 を 読んでOrderedDictを使う、を写経して実行してください
from collections import OrderedDict
od = OrderedDict()
od["a"] = "A"
od["c"] = "C"
od["b"] = "B"
print(od)

d = {}
d["a"] = "A"
d["c"] = "C"
d["b"] = "B"
print(d)

# od から B を削除して下さい
od.popitem()
print(od)


# OrderedDict の公式ドキュメントを探してURLを記述して下さい。
# https://docs.python.org/ja/3/library/collections.html?highlight=ordereddict#collections.OrderedDict

# chap_06_02.md で勉強した dir 関数を使って od が持つメソッドや型を調べてプリントして下さい
print(dir(od))


# ⇑ のメソッドから、 od から値だけ取得するメソッドを探して実行して下さい。
print(od.values())

# P353のタプルからディクショナリを作る、を写経して実行してください
pass 

# P354のsetdefault()メソッドを使う、を写経して実行してください
pass 

# P354のdefalutdict を使う、を写経して実行してください。
pass 

# defaultdictの公式ドキュメントを探してURLを記述して下さい。
# https://docs.python.org/ja/3/library/collections.html?highlight=defaultdict#collections.defaultdict

# P355の bisectモジュールの公式ドキュメントを探してURLを記述して下さい。
# https://docs.python.org/ja/3/library/bisect.html?highlight=bisect#module-bisect


# 以下のリストをソートして下さい
names = ['Emmalyn', 'Sorcha', 'Ina', 'Rennie', 'Blinni']
names.sort() # 破壊的変更
print(names)

# ソートした names にP355の insort_left をつかって Taro を挿入してください。注意：insort_left は bisect モジュールの関数ですので、import する必要があります。OrderedDict をインポートしたコードを参考にしてみてください。

import bisect
bisect.insort_left(names,"Taro")
print(names)

# ソートした names にP355の insort_left をつかって Hanako を挿入してください
bisect.insort_left(names,"Hanako")
print(names)

# ソートした names にP355の insort をつかって shinseitaro を挿入してください
bisect.insort(names,"shinseitaro")
print(names)