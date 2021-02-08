l = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
ints = list(range(5,100,5))
s1 = "Alice was beginning to get very tired of sitting by her sister on the bank and of having nothing to do" 

listmembers = [
    ['Bruis', 'Oxenham', 'boxenham0@ucoz.com', 'Monte Leite'], 
    ['Dacey', 'Inderwick', 'dinderwick1@diigo.com', 'Daxi'], 
    ['Brien', 'Stredwick', 'bstredwick2@nymag.com', 'Seattle'], 
    ['Edan', 'Gooley', 'egooley3@gmpg.org', 'Ghanzi'], 
    ['Celestyna', 'Alwood', 'calwood4@mediafire.com', 'Mainri']
    ]

dictmembers = [
    {'first_name': 'Sven', 'last_name': 'Perago', 'email': 'sperago0@opera.com', 'address': 'Caxias'}, 
    {'first_name': 'Ottilie', 'last_name': 'Babbs', 'email': 'obabbs1@nymag.com', 'address': 'Trondheim'}, 
    {'first_name': 'Zonda', 'last_name': 'Eccleston', 'email': 'zeccleston2@domainmarket.com', 'address': 'Toubao'}, 
    {'first_name': 'Joe', 'last_name': 'Hedaux', 'email': 'jhedaux3@columbia.edu', 'address': 'Sumurgayam'}, 
    {'first_name': 'Katy', 'last_name': 'Ebbles', 'email': 'kebbles4@google.com.br', 'address': 'Paraíso'}
    ]

# l を 逆に並べ替えて下さい
l.reverse()
print(l)

# ints を 逆に並べ替えて下さい
ints.reverse()
print(ints)

# s1 を空白で区切ってリストにして、変数 s2 に代入して下さい
s2 = s1.split(" ")
print(s2)

# l に ints を追加して下さい
l.extend(ints)
print(l)

# dictmembers から3番目の要素を削除して下さい
dictmembers.pop(2)
print(dictmembers)

# l の 'C' のインデックス番号を返して下さい
print(l.index("C"))

# listmembers に、['Chelsae', 'Dasent', 'cdasent1@nasa.gov', 'Longsheng'] を追加して下さい
listmembers.append(['Chelsae', 'Dasent', 'cdasent1@nasa.gov', 'Longsheng'])
print(listmembers)

# dictmembers から last_name だけのリストを作って、変数 lastnames に代入して下さい
lastnames = []
for d in dictmembers:
    lastnames.append(d["last_name"])
print(lastnames)


# listmembers から3番目の要素だけのリストをつくって 変数 emails に代入して下さい
emails = list() 
for l in listmembers:
    emails.append(l[2])
print(emails)

# lastnames と emails を1つのリストにしてください
print(lastnames + emails)

