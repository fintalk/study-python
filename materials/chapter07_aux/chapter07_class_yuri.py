# 成績表のクラスを作成

class RecordBook:
    def __init__(self):
        # データを追加していくための空の辞書を作成。
        self.records = {} 

    def add_students(self, name):
        # 引数に name を取って
        # self.records 辞書にキーを名前、値を空の辞書というデータを追加する。
        # ただし、すでに name が辞書に存在する場合は何もしない
        # if name in self.records:
        #     pass
        # else:
        #     self.records[name] = {}
        if name not in self.records:
            self.records[name] = {}

    def get_records(self):
        # 単純に self.records を返す
        return self.records

    def add_score(self, name, subject, score): 
        # 引数に name, subject, score を取って
        # まずは、self.records に name があるかどうか、なければ追加する。
        # 次にself.records の name キーで取得できる辞書に、{subject: score } を追加する
        self.add_students(name) # (name)はadd_scoreのname。self.にすると__init__で取った引数になる
        self.records[name][subject] = score


    def get_average(self, subject): 
        # 引数に、subject をとって
        # self.records のから subject だけのデータを集め、平均を出す
        # これは最難関です!! がんばってー
        score_list = [i[subject] for i in self.records.values()]
        average = sum(score_list)/len(score_list)
        return average





# RecordBook クラスのインスタンスを作成して、 rb に代入してください
rb = RecordBook() # 空の辞書を作成

# 以下の表の内容を rb に追加してください（平均は不要）

# Name	Math	Music	Gym	Language
# Cissy	81	97	69	58	76.25
# Inglebert	79	82	100	79	85
# Fred	74	67	94	62	74.25
# Ferdie	88	64	89	74	78.75
# Hermon	67	74	81	78	75

students = """Cissy	81	97	69	58
Inglebert	79	82	100	79
Fred	74	67	94	62
Ferdie	88	64	89	74
Hermon	67	74	81	78"""

students_list = []
for student in students.split("\n"): # 1行ずつfor文で回す
    students_list.append(student.split("\t")) # タブで区切る、1行ごとにリストに追加する
# [['Cissy', '81', '97', '69', '58'], ['Inglebert', '79', '82', '100', '79'], ['Fred', '74', '67', '94', '62'], ['Ferdie', '88', '64', '89', '74'], ['Hermon', '67', '74', '81', '78']]

# アンパックを使って変数に代入する
students_list2 = [dict(Name=name, Math=math, Music=music, Gym=gym, Language=language) for name, math, music, gym, language in students_list]
# print(students_list2)

# students_list2 = []
# for name, math, music, gym, language in students_list:
#     students_list2.append(dict(Name=name, Math=math, Music=music, Gym=gym, Language=language))
# [{'Name': 'Cissy', 'Math': '81', 'Music': '97', 'Gym': '69', 'Language': '58'}, {'Name': 'Inglebert', 'Math': '79', 'Music': '82', 'Gym': '100', 'Language': '79'}, {'Name': 'Fred', 'Math': '74', 'Music': '67', 'Gym': '94', 'Language': '62'}, {'Name': 'Ferdie', 'Math': '88', 'Music': '64', 'Gym': '89', 'Language': '74'}, {'Name': 'Hermon', 'Math': '67', 'Music': '74', 'Gym': '81', 'Language': '78'}]

rb = RecordBook()
for d in students_list2:
    rb.add_score(d["Name"],"Math", int(d["Math"]))
    rb.add_score(d["Name"],"Music", int(d["Music"]))
    rb.add_score(d["Name"],"Gym", int(d["Gym"]))
    rb.add_score(d["Name"],"Language", int(d["Language"]))

print(rb.get_records())
print(rb.get_average("Math"))





# def add_students(self, name):
# def add_score(self, name, subject, score): 
# for i in students_list2:
#     rb.add_students(i["Name"])
# {'Cissy': {}, 'Inglebert': {}, 'Fred': {}, 'Ferdie': {}, 'Hermon': {}}




# {'Name': 'Cissy', 'Math': '81', 'Music': '97', 'Gym': '69', 'Language': '58'}
# {'Name': 'Inglebert', 'Math': '79', 'Music': '82', 'Gym': '100', 'Language': '79'}
# {'Name': 'Fred', 'Math': '74', 'Music': '67', 'Gym': '94', 'Language': '62'}
# {'Name': 'Ferdie', 'Math': '88', 'Music': '64', 'Gym': '89', 'Language': '74'}
# {'Name': 'Hermon', 'Math': '67', 'Music': '74', 'Gym': '81', 'Language': '78'}

        # print(j)
# ('Name', 'Cissy')
# ('Math', '81')
# ('Music', '97')
# ('Gym', '69')
# ('Language', '58')




# 失敗1
# for n, math, music, gym, language in students_list:
#     students_list.append(dict(Name=n, Math=s1, Music=, Gym=s3, Language=s4))
# NameError: name 's1' is not defined

# 失敗2
# for n, math, music, gym, language in students_list:
#     students_list.append(dict(Name=n, Math=math, Music=music, Gym=gym, Language=language))
# MemoryError


