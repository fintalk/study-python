# 1. P201の bar() 関数を定義してください。その時リストを１つ引き受ける実装にしてください。

def bar(lst):
    minvalue = min(lst)
    maxvalue = max(lst)
    average = sum(lst)/len(lst)
    return [minvalue, maxvalue, average]

# 2. barに下記のように実行して、コメントのような値がプリントされることを確認してください
# print(bar([1,2,3,4,5,6,7,8,9,10]))
# # (1, 10, 5.5)

print(bar([1,2,3,4,5,6,7,8,9,10]))

# barに下記のように実行して、コメントのような値がプリントされることを確認してください
# minvalue, maxvalue, averagevalue =  bar([1,2,3,4,5,6,7,8,9,10])
# print( minvalue)
# # 1

minvalue, maxvalue, averagevalue =  bar([1,2,3,4,5,6,7,8,9,10])
print(minvalue)