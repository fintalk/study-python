# 1. P369-374 までサラッと目をとおして、いろんなメソッドがあるんだなー、と思ってください。
# pass 

# P375 の正規表現のサンプルを写経して実行してみてください。ただし、一部変更がありますので、以下のように変えて写経してください

import re 
from urllib import request

url = "https://www.python.org/downloads/"

pat = re.compile(r'href="/downloads/release/.+?"')

src = request.urlopen(url).read() 
src = src.decode("utf-8")
for match in pat.findall(src):
    print(match)