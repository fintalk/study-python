# math モジュールの公式ドキュメントを探してURLを記入してください
# pass 

# pi や e は定数です。2つをプリントしてください
import math  
print(math.pi)
print(math.e)

# 2の10乗をmathモジュール内の関数を使って計算しプリントしてください
print(math.pow(2,10))

# 10の平方根をmathモジュール内の関数を使って計算しプリントしてください
print(math.sqrt(10))

# 10の自然対数をmathモジュール内の関数を使って計算しプリントしてください
# 自然対数=ネイピア数の何乗かという意味

print(math.log(10))
#print(math.pow(math.e,math.log(10)))

# 10の常用対数をmathモジュール内の関数を使って計算しプリントしてください
print(math.log10(10))

# random モジュールの公式ドキュメントを探してURLを記入してください
# pass 

# 10以上、100以下のランダムな整数をプリントしてください
import random 
print(random.randint(10,101))

# 10以上、100以下のランダムな整数を続けて10個プリントしてください
# リストでも、１つずつプリントでもいいです。
print(random.sample(range(10,101),10))

# 0以上、1以下のランダムな実数をプリントしてください
print(random.random())


# 0以上、1以下のランダムな実数を続けて10個プリントしてください
print([random.random() for i in range(10)])


# 0以上、1以下のランダムな実数を10個要素に持つリストを変数 random_list に代入してください
random_list = [random.random() for i in range(10)]
print(random_list)

# random_list からランダムに要素を一つ選んでプリントしてください
print(random.choice(random_list))

# random_list をランダムにシャッフルしてプリントしてください
random.shuffle(random_list) # 破壊的変更
print(random_list)

# random_list からランダムに要素を2つ選んでリストにしてプリントしてください
print(random.sample(random_list, 2))