# os モジュールの公式ドキュメントURLを探してください
# pass

# os モジュールをインポートしてください
import os 

# 何かしらの環境変数を getenv()関数を使ってプリントßしてください。これはOSによって違います。環境変数の調べ方は以下を参照してください。

# ホームディレクトリ
print(os.getenv("HOME"))
# 現在のログインユーザ
print(os.getenv("LOGNAME"))

# カレントディレクトリのパスをプリントしてください
print(os.getcwd())

# 以下のディレクトリを os.mkdir を使って作成してください
# os.mkdir("submit/shinseitaro/chap_11_directory_01")

# 以下のディレクトリを makedirs を使って作成してください。
# os.makedirs("./submit/shinseitaro/chap_11_directory_02/child_dir/grand_child_dir")

# mkdir と makedirs はどちらもディレクトリ作成関数ですが、どの部分が違いがありますか？
# どちらも存在しないディレクトリ を作成出来るが、
# mkdir は、１階層のみ
# makedirs は、複数階層を一度に作成出来る

# listdir('submit') をプリントしてください
print(os.listdir("submit"))

# listdir('submit/<your name>') をプリントしてください
print(os.listdir("submit/shinseitaro"))


# exists() 関数を使って、実際に存在するファイルのフルパスを渡し、Trueが返ってくることを確認してください
print(os.path.exists("submit/test.py"))


# exists() 関数を使って、存在しないファイルのフルパスを渡し、Falseが返ってくることを確認してください
print(os.path.exists("submit/hoge.py"))

# 存在するファイルを isfile() 関数に渡しファイルかどうかを確認してください
print(os.path.isfile("submit/test.py"))

# 存在するディレクトリを isdir() 関数に渡しファイルかどうかを確認してください
print(os.path.isdir("submit"))

# join() 関数を使って架空のファイルパスを作成してください。
print(os.path.join("submit","test"))

# 存在するファイルを split() 関数に渡して結果をプリントしてください
print(os.path.split("./chap11/chap_11_09.py"))

# 存在するファイルを dirname() 関数に渡して結果をプリントしてください
print(os.path.dirname("./chap11/chap_11_09.py"))
