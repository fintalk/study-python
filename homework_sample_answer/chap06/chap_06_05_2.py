import math

# 問題

# 履歴書を書くときに必ず書く項目を、年齢以外で5個英語で挙げてください
# name, address, email, birthday, tel

# Resume クラスに上記5個のデータを初期値として引き取るように以下の続きを書いてください
class Resume:
    def __init__(self, name, address, email, birthday, tel):
        self.name = name 
        self.address = address 
        self.email = email 
        self.birthday = birthday 
        self.tel = tel 

    # メールアドレスが記入してあるかどうかを確認するクラスメソッドを定義してください。
    def exist_email(self):
        if self.email:
            return True 
        else:
            return False

# Resumeクラスのインスタンスを作って、 resume1 に代入してください。    
resume1 = Resume("Taro Okamoto", "Shinjuku, Tokyo", "taro@taro.com", "1911-2-26", "11-1111-1111")

print(resume1.name )
print(resume1.address )
print(resume1.email )
print(resume1.birthday )
print(resume1.tel )

# resume2 インスタンスを作って同様に参照プリントしてください。
resume2 = Resume("Kanoko Okamoto", "Akasaka, Tokyo", "kanoko@taro.com", "1889-3-1", "11-1111-1111")
print(resume2.name )
print(resume2.address )
print(resume2.email )
print(resume2.birthday )
print(resume2.tel )


# 直角三角形を作るクラス RightTriangle を 作ってください。以下の初期値とクラスメソッドを持たせてください

class RightTriangle:
    def __init__(self, bottom, height, name, color):
        self.bottom = bottom
        self.height = height
        self.name = name 
        self.color = color 

    def area(self):
        return self.bottom * self.height * 0.5 
    
    def hypotenuse(self):
        return (self.bottom**2 + self.height**2) ** 0.5 

        # これでもいいよ。
        # import math
        # return math.sqrt(self.bottom**2 + self.height**2) 
    
    def degrees(self):
        a = 90
        b = math.degrees(math.atan(self.height/self.bottom))
        c = 180 - (a + b)
        return (a, b, c)

r = RightTriangle(5, 9, "oira", "red")
# print(r.degrees())
# print(r.hypotenuse())

print(r.name)


