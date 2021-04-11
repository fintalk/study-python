# P339 までさらっと読んでください
# pass 

# filelen.py を新規作成して、P338の filelen.py を写経してください
# はい

# 下記を実行してください
# $ python filelen.py chap_10_01.py

# 今度は存在しないファイルへのパスを与えて、「〜〜〜というファイルは存在しません」とプリントされるか確認してください

# $ python filelen.py chap_10_1000.py 
# chap_10_1000.py というファイルは存在しません

# 色々例外を出していきましょうー。以下を写経して実行してください。 
# pass 

# try ~ except 文の練習をたくさんしていきましょう. 下記をコメントも含めて写経して実行して下さい。
# pass 

# 同様の方法で、以下のエラーを出すコードを書いて、エラーが出ないように書き直して下さい。

# -------------------------------------------------------
# IndentationError 
#    print("ハロー")

#   File "chap_10_01.py", line 24
#     print("ハロー")
#     ^
# IndentationError: unexpected indent

# ただしくは
# print("ハロー")

# -------------------------------------------------------
# IndexError
# lst = [1,2,3]
# print(lst[100]) 

# Traceback (most recent call last):
#   File "chap_10_01.py", line 26, in <module>
#     print(lst[100]) 
# IndexError: list index out of range

# ただしくはこれなど
# print(lst[1]) 
# -------------------------------------------------------
# TypeError
# stock = 20
# '10' + stock

# File "chap_10_01.py", line 50, in <module>
#     '10' + stock
# TypeError: can only concatenate str (not "int") to str

# ただしくは
# stock = 20
# int("10") + stock

# -------------------------------------------------------
# FileNotFoundError
# open("hoge.py")
# Traceback (most recent call last):
#   File "chap_10_01.py", line 62, in <module>
#     open("hoge.py")
# FileNotFoundError: [Errno 2] No such file or directory: 'hoge.py'

# ただしくは、存在するファイルパスをちゃんと渡す

# -------------------------------------------------------
# KeyError
# d = {"a":10, "b": 20}
# d["c"]
# File "chap_10_01.py", line 73, in <module>
#     d["c"]
# KeyError: 'c'

# -------------------------------------------------------
# ModuleNotFoundError

# import shinseitaro
# Traceback (most recent call last):
#   File "chap_10_01.py", line 80, in <module>
#     import shinseitaro
# ModuleNotFoundError: No module named 'shinseitaro'

# -------------------------------------------------------
# ImportError
# from datetime import datetimeeee
# Traceback (most recent call last):
#   File "chap_10_01.py", line 89, in <module>
#     from datetime import datetimeeee
# ImportError: cannot import name 'datetimeeee' from 'datetime' 

# -------------------------------------------------------

