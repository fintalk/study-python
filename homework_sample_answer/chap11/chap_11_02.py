# datetime の公式ドキュメントのURLを探して下さい
# https://docs.python.org/ja/3/library/datetime.html?highlight=datetime#datetime.datetime

# datetime モジュールをインポートして下さい
import datetime 

# datetime インスタンスオブジェクトを、2021年1月2日 で作成して、変数 dt1 に代入して下さい。
dt1 = datetime.datetime(2021,1,2)
print(dt1)

# datetime インスタンスオブジェクトを、2000年1月2日 19:52 で作成して、変数 dt2 に代入して下さい。
dt2 = datetime.datetime(2000,1,2, 19, 52)
print(dt2)

# dt2 のアトリビュートや関数を dir を使って調べて下さい
print(dir(dt2))

# dt1, dt2 の 年だけをプリントしてください
print(dt1.year)
print(dt2.year)

# datetime インスタンスオブジェクトを、現在の日時 で作成して、変数 dt3 に代入して下さい。
dt3 = datetime.datetime.now()
print(dt3)


# P358 の strftime() メソッドと、フォーマット文字列を使って dt2 を 以下の文字列に変換して下さい。例をみてトライしてみてください。

# '2000-01-02'
print(dt2.strftime("%Y-%m-%d"))

# '2000年01月02日'
print(dt2.strftime("%Y年%m月%d日"))

# '2000-01-02 19:52'
print(dt2.strftime("%Y-%m-%d %H:%M"))

# '2000-01-02 19:52 Sunday'
print(dt2.strftime("%Y-%m-%d %H:%M %A" ))

# '2000-01-02 19:52 Sun'
print(dt2.strftime("%Y-%m-%d %H:%M %a" ))

# '2000-01-02 PM 07:52'
print(dt2.strftime("%Y-%m-%d %p %I:%M" ))



# P359 の stfptime() メソッドを使って、以下の文字列から datetimeインスタンスオブジェクトを作成してください。例をみてトライしてみてください。
# # 例
# datetime.strptime("2020-01-01", "%Y-%m-%d")
# # datetime.datetime(2020, 1, 1, 0, 0)
# '2000-01-02'
# '2000年01月02日'
# '2000-01-02 19:52'
# '2000-01-02 19:52 Sunday'
# '2000-01-02 19:52 Sun'
# '2000-01-02 PM 07:52'