import random

def fizzbuzz(i):
    if i%3 == 0 and i%5==0:
        raise ValueError(f"{i} は3でも5でも割り切れるぞ")
    return i 
        
for i in random.sample(range(1000, 10000), 99):
    print(fizzbuzz(i))

