# date オブジェクト の公式ドキュメントのURLを探してください
# https://docs.python.org/ja/3/library/datetime.html?highlight=date#datetime.date

# dateクラスを使って、2021/01/03の dateオブジェクトを作成し、変数 d1 に代入してください
import datetime
d1 = datetime.date(2021,1,3)

# P361の timetuple を使って、d1 の日付をタプルで取得してプリントしてください
print(d1.timetuple())

# P362の weekday を使って曜日番号を取得してプリントしてください
print(d1.weekday())

# P362の isoweekday を使って曜日番号を取得してプリントしてください
print(d1.isoweekday())

# datetime オブジェクト の公式ドキュメントのURLを探してください
# https://docs.python.org/ja/3/library/datetime.html?highlight=datetime#datetime.datetime

# datetime インスタンスオブジェクトを、現在の日時 で作成して、変数 dt1 に代入して下さい。
dt1 = datetime.datetime.now() 

# P362の date メソッド を使ってdateクラスのインスタンスを取得してください
print(dt1.date())

# P362の time メソッド を使ってtimeクラスのインスタンスを取得してください
print(dt1.time())