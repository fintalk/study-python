# P144 の for 文と else 文の組み合わせを写経して実行して下さい
# pass 

#以下の name_list に関して、for 文と else 文の組み合わせを使って Tiena と Taro が入っているかどうかを確認し、入っていない場合は、入っていない旨をプリントして下さい

name_list = ['Aland', 'Dari', 'Lorelle', 'Debbie', 'Jermaine', 'Royal', 'Tiena', 'Adelice', 'Vivyanne', 'Rosco']

for name in name_list: 
    if name in ["Tiena", "Taro"]:
        print(name, "がいました")
        break
else:
    print("Tiena と Taro はいません")