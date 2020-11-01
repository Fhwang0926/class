#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926

whatever_list = [1, 2, 3]
whatever_tuple = (1, 2, 3) # 요수 추가 혹은 수정이 불가


for item in whatever_list:
    item = 1
    print("list item", item)
    pass
whatever_list[0] = 0
print("list all", whatever_list)

print("##################################")

for item in whatever_tuple:
    item = 1
    print("tuple item", item)
    pass
whatever_list[0] = 0
# whatever_tuple.append(1)
print("tuple all", whatever_tuple)

test_dict = { 'key' : 1 }

print(test_dict)
test_dict['name'] = 'hdh'
print(test_dict)