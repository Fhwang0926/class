#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
import time
whatever = [1, 2, 3]

# 1. for
for number in whatever:
    print('number', number)
    pass

for number in range(0, 10):
    print('number', number)
    pass
print("#############")
# 2. while
loop = 0
while loop<10:
    time.sleep(1) # 없으면 계속 실해오디기에 무조건 필요
    loop+=1
    print('loop', loop)
    pass
print("#############")

loop = 0
while 1:
    time.sleep(1) # 없으면 계속 실해오디기에 무조건 필요
    loop+=1
    print('loop', loop)
    if loop >= 10:
        print("loop break", loop)
        break
    pass