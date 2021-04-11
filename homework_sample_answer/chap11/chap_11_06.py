# P365−367までさらっと読んでください
pass 

# re モジュールをインポートしてください。
import re 

# compile() 関数を使って正規表現オブジェクトを作りましょう。
# 郵便番号は「３桁数値-４桁数値」です。このパターンを使って正規表現オブジェクトを作り、変数 postal_pattern に代入してください

postal_pattern = re.compile("\d\d\d-\d\d\d\d")

# print(postal_pattern.match("123-1234")) を実行して、re.Match object がプリントされるか確認してください
print(postal_pattern.match("123-1234"))

# print(postal_pattern.match("1231234")) を実行して、None がプリントされるか確認してください
print(postal_pattern.match("1231234"))

# print(postal_pattern.match("ABC-ABCD")) を実行して、None がプリントされるか確認してください
print(postal_pattern.match("ABC-ABCD"))


# 「」に囲まれた文字列にマッチする正規表現オブジェクトを作り、変数 quote_pattern に代入してください。
# ヒント1:「」はそのままつかってよい
# ヒント2:「」の中に、どんな文字にもマッチするメタ文字を、1回以上繰り返し
# ヒント3:直前にあるパターンを0もしくは1回以上繰り返す

quote_pattern = re.compile("「.+?」")
#quote_pattern = re.compile("「[^「]*」")

# quote_pattern.findall("しんせいたろう") をプリントして、空のリストが返ることを確認してください
# findall() メソッドはP370に記載されています。
print(quote_pattern.findall("しんせいたろう") )

# quote_pattern.findall("しんせい「たろう」")をプリントして、['「たろう」'] が返ることを確認してください
print(quote_pattern.findall("しんせい「たろう」"))


# 上記「正規表現はいつ使う？」の中で作ったs2 を使って、quote_pattern.findall(s2) をプリントし以下のリストがプリントされることを確認してください。
# ['「高潔な」', '「正しい」', '「公平な」', '「名誉な」', '「閣下」', '「Right」', '「全く」', '「まことに」']

s2 = """オナラブル（英語: The Honorable）とは、「高潔な」「正しい」「公平な」、あるいは「名誉な」という意味。イギリス連邦各国では、首相や閣僚、カナダやオーストラリア・ニュージーランドなどの総督、一部の貴族、大使、大都市の首長に対する敬称或いは儀礼称号。アメリカでは裁判官、判事などにも付けられる。日本語の「閣下」に相当し[1]、名前の前に"The Right Honorable（The Rt. Hon.）"を付けて表記される。 (ここでの「Right」は「全く」「まことに」といった意味である) たとえばイギリスの政治家デーヴィッド・キャメロンの場合だと、"The Right Honorable David Cameron"となる。"""

print(quote_pattern.findall(s2) )
