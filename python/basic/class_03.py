#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926


# 1. 조건문
if 1 == 1:
    print('1 == 1', 'sure')
else:
    print('1 == 1', 'not sure')

# 2. 비교 연산자 또는 논리 연산자
print('1 == 1 is ', 1 == 1)
print('1 < 1 is ', 1 < 1)
print('1 <= 1 is ', 1 <= 1)
print('1 > 1 is ', 1 > 1)
print('1 >= 1 is ', 1 >= 1)
print('1 != 1 is ', 1 != 1)

# and, or not()
# 3. if and double if
if 1 == 1 and 2 == 2:
    print("by and")

if 2 == 1 or 2 == 2:
    print("by or")

if not 2 == 1:
    print("by not")

# 4. if and double if
if 1 == 1 and 2 == 2:
    print("all same")
elif 1 == 1:
    print("only 1 same")
else:
    print("only 2 same")
