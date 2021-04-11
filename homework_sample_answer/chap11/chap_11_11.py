# urllib.request モジュールの公式ドキュメントを探してURLを記入してください
# pass 
# urllib.request をインポートしてください。
import  urllib.request

# urlretrieve() 関数を使って日経平均株価をダウンロードしてみましょう。URLは、 https://indexes.nikkei.co.jp/nkave/historical/nikkei_stock_average_daily_jp.csv ダウンロード先は、submit/<your name>/nikkei.csv を指定してください。


# 解答
# urllib.request.urlretrieve(
#     "https://indexes.nikkei.co.jp/nkave/historical/nikkei_stock_average_daily_jp.csv",filename="./submit/shinseitaro/nikkei.csv ")


# urlopen関数をつかって google のトップページを取得し、変数 obj に代入してください。URLは https://www.google.com/ です

obj = urllib.request.urlopen("https://www.google.com/")

# objのデータをすべて読み込んでください。
print(obj.read())

# objのデータを最初の一行だけ読み込んでください（いったん読み込んだファイル風オブジェクトはデータを吐き出した状態になりますので、objを再作成する必要があります。）
obj = urllib.request.urlopen("https://www.google.com/")
print(obj.readline())

# objのデータを全行読み込んでください
obj = urllib.request.urlopen("https://www.google.com/")
print(obj.readlines())


# objからデータを取得したURLを取得してください
print(obj.geturl())