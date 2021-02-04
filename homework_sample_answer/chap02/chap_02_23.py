# リストを1つ引数にとって最も大きい数値を返す関数 my_max 関数を定義して下さい
def my_max(l):
    return max(l)

# リストを1つ引数にとって最も小さい数値を返す関数 my_min 関数を定義して下さい
def my_min(l):
    return min(l)

# リストを1つ引数にとって平均を返す関数 my_mean 関数を定義して下さい
def my_mean(l):
    return sum(l) / len(l)

# 以下の条件を満たす関数 get_results を記述して下さい。
# 引数はリストを1つ取る。ただし、そのリストは複数のリストを要素として持つリスト（二次元リスト）とする
# 各リストに対して、my_max, my_min, my_mean の結果をリストに入れて、プリントする
# 返り値は無し
def get_results(lists):
    for l in lists:
        print([my_max(l), my_min(l), my_mean(l)])

# get_results に lists を渡して実行して下さい。実行結果通りであれば正解です。
list1 = [142, 236, 172, 223, 139]
list2 = [164, 101, 159, 131, 187]
list3 = [196, 134, 124, 206, 217]
lists = [list1, list2, list3]

# >>> get_results(lists)
# [236, 139, 182.4]
# [187, 101, 148.4]
# [217, 124, 175.4]    

get_results(lists)

# 下記の条件を満たす fortune_telling 関数を定義して下さい。
# 数値の引数を１つ受取る
# very lucky day, unlucky day, not too bad の３つを持つリストを定義
# 受け取った引数を使って、リストの中から１つランダムに要素を返す

def fortune_telling(n):
    terms = ["very lucky day", "unlucky day", "not too bad"]
    # この記述だと何回か試すとどの数字であればどの言葉が出るかバレてしまうが、
    # ここでランダムにすると、そもそも n を入れた意味もなくなるので、あえてこのようにしました。
    i = int(float(n)) % len(terms)
    return(terms[i])

# input 関数を使って、数値を取得し、それを fortune-telling 関数に渡して結果を実行するコードを書いて実行して下さい。
n = input("好きな数字を渡して下さい")
print(fortune_telling(n))