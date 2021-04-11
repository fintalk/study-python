# P363 の weekday() メソッドを使って、2021年1月3日の曜日番号を取得してプリントしてください
import calendar 
print(calendar.weekday(2021, 1,3))

# コレと一緒です
# import datetime 
# print(datetime.date(2021,1,3).weekday())


# P363 の monthrange() メソッドを使って、2021年1月の月初めの曜日と、月の日数を取得してプリントしてください
print(calendar.monthrange(2021,1))


# 今年の1月〜12月までの月初めの曜日と、月の日数を取得してプリントしてください。for を使ってループを回しながらプリントしてください。
for i in range(1,13):
    print(f"{i}月", calendar.monthrange(2021,i))
    

# month()メソッドを使って、今月のカレンダーを表示してください
print(calendar.month(2021, 3))


# monthcalendar() メソッドを使って、今月のカレンダーを表示してください
print(calendar.monthcalendar(2021, 3))

# 今年がうるう年かどうか確認してください
print(calendar.isleap(2021))
