# timedelta オブジェクトの公式ドキュメントのURLを貼ってください
# https://docs.python.org/ja/3/library/datetime.html?highlight=timedelta#datetime.timedelta

# P360 の 日時の差を求める、を写経して実行してください。
pass 

# 2021/01/03 と 2021/01/01 の日時の差を求めてください。
import datetime
d1 = datetime.date(2021,1,3)
d2 = datetime.date(2021,1,1)
print(d1 - d2 )

# 2021/01/03 午前9時6分 と 2021/01/01 午前10時30分 の日時の差を求めてください。
dt1 = datetime.datetime(2021,1,3, 9, 6)
dt2 = datetime.datetime(2021,1,1, 10, 30)
print(dt1 - dt2 )

# 現在時刻から、オリンピック開会式 2021年7月23日（金） 20:00までの日時の差を求めてください
dt4 = datetime.datetime.now() 
gorin = datetime.datetime(2021,7,23, 20,0)
print(gorin - dt4)

# P360 の 日時の加算を求める、を写経して実行してください。
pass 
# 2021/01/01 に 100日追加した日付を求めてください
print(datetime.date(2021,1,1) + datetime.timedelta(days=100))


# 2021/01/03 午前9時6分 に3日と100分追加した日時を求めてください
print(datetime.datetime(2021,1,3, 9,6) + datetime.timedelta(days=3, minutes=100))

# P361の日時の掛け算割り算、を写経して実行してください。
pass 

# P361の日時の比較、を写経して実行してください。
pass 

# datetime インスタンスオブジェクトを、現在の日時 で作成して、変数 dt1 に代入して下さい。
dt1 = datetime.datetime.now() 

# dt1 から2日引いたオブジェクトを作成して dt2 に代入してください
dt2 = dt1 - datetime.timedelta(days=2)
print(dt2)

# dt1がdt2より未来であることを比較演算子を使って確認してください
print(dt1 > dt2)
# dt1とdt2は、等価ではないことを比較演算子を使って確認してください
print(dt1 != dt2)