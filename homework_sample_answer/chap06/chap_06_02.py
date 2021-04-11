# P255 ~ P256 のDecimalクラスを使う準備、Decimalクラスを使う、インスタンスを使った演算、を写経して実行してください。
# pass 

# P257 の Decimal 型を使った比較、を写経して実行してください。
# pass 

# P257 平方根を計算する、を写経して実行してください。
# pass 

# ....
# この中から、「ゼロかどうか確認するメソッド」を名前から探して d に対して実行してみてください

from decimal import Decimal
d = Decimal(10)
print(dir(d))
print(d.is_zero())