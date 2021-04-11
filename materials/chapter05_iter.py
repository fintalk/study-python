from time import time
def test():
    for i in range(0, 10**8):
        if i == 0:
            break
start_time = time()
test()
end_time = time()

# python2 
# print end_time-start_time

# python3
print(end_time-start_time)