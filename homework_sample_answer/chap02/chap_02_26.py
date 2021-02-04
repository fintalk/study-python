# 日時を扱う datetime モジュールを探し、現在のローカルな「日付」を返す。（ローカルな＝自分のパソコンが存在する地域のこと）

from datetime import datetime, date # from 文を使う時、カンマ区切りにすれば複数のメソッドをインポートすることもできます。
print(date.today())

# 同モジュールで、現在のローカルな「日時」を返す。
print(datetime.now())

# オペレーションシステムインターフェイスを扱う os モジュールを探し、指定したパスのディレクトリを作成する関数を探して実行して下さい。
import os 
os.mkdir("ここに文字列で作成したいパスを記述して下さい")
# 注意：Mac/Linuxの場合は、ファインダーなどで表示されているパスを書けばよいですが 
# windows の場合は区切り文字が [\\] になります。
# 例 : c:\Program Files\myfolder\test というディレクトリを作成したい
# os.mkdir("c:\\Program Files\\myfolder\\test")

# 同モジュールで、指定したパスのディレクトリを「再帰的」に作成する関数を探して実行して下さい
os.makedirs("ここに文字列で作成したいパスを記述して下さい")
