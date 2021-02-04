# P181のf文字列を使った例を写経してプリントして下さい。
# pass 

# f文字列をつかって以下の文字列で、"Tokyo Olympic has postponed to 2021" とプリントして下さい
year = 2021
event = "Tokyo Olympic"
print(f"{event} has postponed to {year}")

#では以下の数値を小数点一位且つ、1000の位でカンマが入った文字列にｆ文字列を使って変換しプリントしてください。
n1 = 1520364.0041
n2 = 0.0052
n3 = 10

print(f"{n1:,.1f}")
print(f"{n2:,.1f}")
print(f"{n3:,.1f}")

# 以下の数値を全て、小数点3位且つ、％表記の文字列に変換してプリントしてください
n1 = 10/10.5
n2 = 0.0052
n3 = 10

print(f"{n1:.3%}")
print(f"{n2:.3%}")
print(f"{n3:.3%}")
