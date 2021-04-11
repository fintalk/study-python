# 成績表のクラスを作成

class RecordBook:
    def __init__(self):
        # データを追加していくための空の辞書を作成。
        self.records = {} 

    def add_students(self,name):
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

    def add_score(self,name, subject, score): 
        # 引数に name, subject, score を取って
        # まずは、self.records に name があるかどうか、なければ追加する。
        # 次にself.records の name キーで取得できる辞書に、{subject: score } を追加する
        self.add_students(name)
        self.records[name][subject] = score

    def get_average(self, subject): 
        # 引数に、subject をとって
        # self.records から subject だけのデータを集め、平均を出す
        # これは最難関です!! がんばってー
        t_Math = self.records[Math]/self.records #何人いるかをカウントして割る
        t_English = self.records[English]
        
        #subjectごとにスコアを抽出　subjectの数で割る
        pass #TODO できたらスラックで報告

rb = RecordBook()
# print(rb.records)
# {}

rb.add_students("Taro")
# print(rb.records)

print(rb.get_records())

rb.add_score("Hanako","Math",100)
print(rb.get_records())
 # {'Taro': {}, 'Hanako': {'Math': 100}}

rb.add_score("Hanako","English",30)
print(rb.get_records())
 # {'Taro': {}, 'Hanako': {'Math': 100, 'English': 30}}

rb.add_score("Taro","Math",55)
print(rb.get_records())


