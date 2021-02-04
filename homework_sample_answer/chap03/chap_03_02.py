# P122 の convert_number() 関数を写経して下さい．
# pass 

# convert_number() で，変換できる num を入れて実行して下さい
# pass 

# convert_number() で，変換できない num を入れて実行して下さい
# pass 

# 以下のテーブルを参考にして、ヘッダーをキーにデータを値に持つ辞書を作って下さい。その際、first_name を変数名にして辞書を定義して下さい。
Sanderson = {'first_name': 'Sanderson', 'email': 'slettington0@examiner.com', 'company': 'Kimia'}
Lanni = {'first_name': 'Lanni', 'email': 'lrosenblatt1@sitemeter.com', 'company': 'Pixonyx'}
Margot = {'first_name': 'Margot', 'email': 'mdelgua2@qq.com', 'company': 'Voolia'}


# 以下の条件で get_company関数を作成して下さい
# 引数に辞書を一つ引き取る
# 辞書に "company" キーが存在すれば，その値を返す
# なければ，"no company" を 返す
def get_company(d):
    if "company" in d:
        return (d["company"])
    else:
        return ("no comnay")

print(get_company(Sanderson))
print(get_company(Lanni))
print(get_company(Margot))


