import random 

def myfunc(test_list):
    try:
        for i in test_list:
            10 / i
        print("ゼロはありませんでした！", test_list)
    except ZeroDivisionError: # 
        print("ゼロが見つかりました！", test_list)
    except: 
        print("未知のエラーが発生しました", test_list)

# -10 から 10 の数値をランダムに10個並べたリストを作成
myfunc(random.sample(range(-10, 10), 10))
myfunc(random.sample(range(-10, 10), 10))
myfunc(random.sample(range(-10, 10), 10))
myfunc(random.sample(range(-10, 10), 10))



