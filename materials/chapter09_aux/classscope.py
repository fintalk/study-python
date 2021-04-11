from datetime import date 

class Resume:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    
    def age(self): 
        # pythonの標準クラス datetime の中に定義してある today() メソッド
        today = date.today()
        # self.が保持しているデータを使う。 
        days = (today - self.birthday).days # 日数を数値で取得
        years = round(days / 365) # 365で割って年数を出す
        return years
        

r1 = Resume("okamoto taro", date(1911,2,26))
print(r1.age())

r2 = Resume("山田花子", date(1975,3,10))
print(r2.age())

#r1.age = 5000
#print(r1.age())

Resume.age = 500 

print(r2.age())
