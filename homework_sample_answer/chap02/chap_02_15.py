# P90の2重の if文を使用した例を写経して実行して下さい．
# pass 

# address に "東京都千代田区永田町1−7−1" を代入して下さい
address = "東京都千代田区永田町1−7−1"

# word に "千代田区" を代入してください
word = "千代田区"

# もし，address に word が入っているならば，address に "永田町"が入っているかどうかをif 文で書いて下さい．入っていればTrue,入っていなければFalseをプリントしてください
if word in address:
    if "永田町" in address:
        print("True")
    else:
        print("False")

# P91 の elif文の使用例を写経して下さい．
# pass 


# P91 の elif文の使用例の「1993」をb_year に代入して，全体を書き換えて実行してください．
a_year = 2080
b_year = 1993 
if a_year == b_year:
    print(a_year, "年、れに誕生")
elif a_year > b_year:
    print(a_year, "年、れに", a_year-b_year, "歳")

# a_yearと b_year を適当に書き換えてコードを実行してみてください．

a_year = 2100
b_year = 2000 
if a_year == b_year:
    print(a_year, "年、れに誕生")
elif a_year > b_year:
    print(a_year, "年、れに", a_year-b_year, "歳")

