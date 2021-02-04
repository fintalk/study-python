# P179のキーで差し込み位置を指定する、を写経して実行して下さい.
# pass 

# 以下の名前リストを使って、"My name is [名字], [名前] [名字]."の形でプリントして下さい。
namelist = [
        {"first_name": "Iona","last_name": "Batting"}, 
        {"first_name": "Abner", "last_name": "Baynom"}, 
        {"first_name": "Cale","last_name": "Brighouse"}, 
        {"first_name": "Janice", "last_name": "Golby"},
    ]
for dict_name in namelist: 
    print("My name is {last_name}, {first_name} {last_name}".format(**dict_name))

# P179のディクショナリで差し込み位置を指定するを写経してプリントして下さい    
