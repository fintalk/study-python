# 引数 obj を一つとって，objが True なら「YES」 False なら 「No」をプリントする関数 `check()` を作って下さい。ただし引数 obj は組み込み型オブジェクトを想定しています。

def print_args(func): 
    def _print(*args):
        print("引数", args)
        return func(args)
    return _print


@print_args
def check(obj):
    if obj:
        print("YES")
    else:
        print("NO")

# check関数に以下のデータを渡して，各々実行して下さい
s1 = "ABC"
l1 = []
d1 = {}
s2 = ""
l2 = list("ABC")
d2 = {"name": "Zane Piet", "born": 2009, "tel": "796-824-5240"}


check(s1)
check(l1)
check(d1)
check(s2)
check(l2)
check(d2)
