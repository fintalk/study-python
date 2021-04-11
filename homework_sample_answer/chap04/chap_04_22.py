ozzi =  {"name": "Ozzie Poupard",  "born": 2006,  "tel": "369-508-7178"}
people = [
    {'name': 'Valerye Astridge', 'born': 2006, 'tel': '363-627-4586'}, 
    {'name': 'Ozzie Poupard', 'born': 2006, 'tel': '369-508-7178'}, 
    {'name': 'Homer Moulsdall', 'born': 2010, 'tel': '130-701-0215'}, 
    {'name': 'Shoshana Lowndsborough', 'born': 1997, 'tel': '868-580-7258'}, 
    {'name': 'Zane Piet', 'born': 2009, 'tel': '796-824-5240'}]

# 1. ozzi のキーのみを取得して下さい
print(ozzi.keys())

# 2. ozzi から name を取得して下さい
# どちらでもOK
print(ozzi.get("name")) 
print(ozzi["name"]) 


# 3. ozzi から age を取得しようとすると None が返ってくることを確認して下さい
print(ozzi.get("age")) 

# 4. people の各辞書から値だけを取得して下さい
for d in people:
    print(d.values())

# ozzi でキーと値のタプルを取得して下さい
print(ozzi.items())

# people の各辞書をキーと値のタプルにしてください
for d in people:
    print(d.items())


# ozzi の電話番号を "111-111-1111" に更新して下さい
ozzi["tel"] = "111-111-1111"
print(ozzi)
