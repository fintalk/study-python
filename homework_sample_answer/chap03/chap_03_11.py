# P140のFizzBuzz問題を解くプロブラムを写経して実行して下さい
# pass 

# 1〜１００までの数値で，3の倍数と3がつく数値の時だけアホとプリントするプログラムを書いて下さい．参照：https://www.youtube.com/watch?v=ntWfk25G7Vg
# 3がつく数値 という処理をどのように書くかがポイント
# 恐らく一番簡単なのは，list関数を使うことです．
# list 関数に文字列を渡すと，一つずつバラにしてリストにして返します．これを使ってみて下さい．
# >>> list("123456")
# ['1', '2', '3', '4', '5', '6']
# もしくはstr関数は数値を受け取って文字列を返す関数を使ってもよいかもしれません
# >>> str(123)
# '123'

cnt = 1 
while cnt <= 100:
    if cnt % 3 == 0:
        print(cnt, "アホ")
    elif str(3) in list(str(cnt)):
        print(cnt, "アホ")
    else:
        print(cnt)
    cnt += 1