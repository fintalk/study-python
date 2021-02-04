# P177のフォーマットに文字列を差し込む、を写経して実行して下さい
# pass 

# formatメソッドを使って、文字列 "Hello I am {}！" にご自身の名前を差し込んでプリントして下さい
print("Hello I am {}！".format("しんせいたろう"))

# P178の複数を同時に差し込む、を写経して実行して下さい
# pass 

# 下記リストを使って、"Hello I am ~~~!" という絵文字列を一人ずつに作ってプリントして下さい。
names = ['Antonino', 'Natale', 'Torey', 'Beverly', 'Othilia']
for name in names:
    print("Hello I am {}！".format(name))


# P178の数値で差し込み位置を指定する、を写経して実行して下さい
# pass 

# 差し込み位置を指定する方法で、"My name is [名字], [名前] [名字]."  で "My name is Bond, James Bond." とプリントして下さい
print("My name is {1}, {0} {1}.".format("Jame", "Bond"))


# 下記リストを使って、"My name is [名字], [名前] [名字]." の形でプリントして下さい
names = [['Ricky,Champness'], ['Rozanna,Avann'], ['Booth,Howlin'], ['Zonnya,Dadd'], ['Adelbert,Yule']]
for x in names: 
    # x は ['Ricky,Champness'] という形で、文字列一つが入ったリスト
    # よってここから名前と名字を分けるには、
    # x[0] で、文字列を取得したあと、split(",")する
    given_name = x[0].split(",")[0]
    family_name = x[0].split(",")[1]
    print("My name is {1}, {0} {1}.".format(given_name, family_name))
    
