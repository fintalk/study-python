# 問題
# 1. 
from datetime import date 

class Resume: #スーパークラス
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
    
    def age(self): 
        # pythonの標準クラス datetime の中に定義してある today() メソッド
        today = date.today()
        # self.が保持しているデータを使う。 
        days = (today - self.birthday).days
        years = round(days / 365)
        return years


class CurriculumVitae(Resume): # サブクラス
    pass 

# 2. 
cv = CurriculumVitae("okamoto taro", date(1911, 2, 26))

# 3. 

print(cv.name)

# class CurriculumVitae(Resume): # サブクラス
#     def __init__(self, objective, summary):
#         self.objective = objective
#         self.summary = summary

class CurriculumVitae(Resume): # 
    #サブクラスのインスタンスが取得すべきデータの引数を全て渡す。
    def __init__(self, name, birthday, objective, summary) : 
        # スーパークラスを呼び出し、init関数を呼び出して、name と birthday を保存
        super().__init__(name, birthday) 
        # 他のデータを通常通り保存
        self.objective = objective
        self.summary = summary


cv2 = CurriculumVitae(
    "shinseitaro",      # スーパークラスの name 
    date(2000,1,1),     # スーパークラスの birthday
    "社長",              # サブクラスの objective
    "プーたろうしてました"  # サブクラスの summary
    )

print(cv2.name)
print(cv2.birthday)
print(cv2.objective)
print(cv2.summary)


# 問題
# 1. 

class CurriculumVitae(Resume): # 
    def __init__(self, name, birthday, objective, summary) : 
        super().__init__(name, birthday) 
        self.objective = objective
        self.summary = summary

    def is_pythonista(self):
        if "python" in self.summary:
            return "pass"
        else:
            return "failed"
    
cv3 = CurriculumVitae(
    "okamoto taro",
     date(1911, 2, 26), 
     "art director",
     "大阪万博の太陽の塔を作った"
)    

print(cv3.is_pythonista())


class CurriculumVitae(Resume): # 
    def __init__(self, name, birthday, objective, summary) : 
        super().__init__(name, birthday) 
        self.objective = objective
        self.summary = summary

    def is_pythonista(self):
        if "python" in self.summary:
            return "pass"
        else:
            return "failed"
    
    def age(self):
        return super().age() >= 20 


cv4 = CurriculumVitae(
    "okamoto taro",
     date(1911, 2, 26), 
     "art director",
     "大阪万博の太陽の塔を作った"
)  

print(cv4.age())

# まとめ問題

class BankAccount:
    def __init__(self, name, address, initial_deposit):
        self.name = name 
        self.address = address
        self.initial_deposit = initial_deposit
        self.balance = self.initial_deposit

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
class AccountInfo(BankAccount):
    def is_minus_balance(self):
        return self.balance < 0 
    
    def is_payoff_account(self):
        return self.balance > 10000000 

    
ai = AccountInfo("okamoto taro", "川崎市", 1000000)
print(ai.balance)
ai.deposit(123)
print(ai.balance)
print(ai.is_payoff_account())


    



