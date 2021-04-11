# 1. P201 で説明している foo() 関数を記述してください。その際、2つの引数をひきとりその値をリストで返すように記述してください。

def foo(valuea, valueb):
    return [valuea, valueb]

# 2. foo()に、2つの変数 "a" "b" をわたし、
# alist = foo("a", "b")
# print(alist[0])
# を実行し、"a" が返ることを確認してください

alist = foo("a", "b")
print(alist[0])

# 3. 引数、first_name と last_name を引取り、2つの名前をタプルに入れて返す関数 get_fullname() を定義してください。

def get_fullname(first_name, last_name):
    return (first_name, last_name)

# 4. 下記のようにプリントされるか確認してください(コメントアウトが答えです)
# print(get_fullname('Luelle', 'Shevels'))
# # ('Luelle', 'Shevels')
print(get_fullname('Luelle', 'Shevels'))


# 5. 下記のようにプリントされるか確認してください
# family_name = get_fullname('Luelle', 'Shevels')[1]
# print(family_name)
# # 'Shevels'

family_name = get_fullname('Luelle', 'Shevels')[1]
print(family_name)
