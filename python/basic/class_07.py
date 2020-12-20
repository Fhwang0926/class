#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
# 사용자 정의 모듈 임포트
from module.item import Car

# 클래스로 인스턴스(객채 생성)
item = Car()

print(item)
print(item.category)
print(item.number)
item.update()
print(item.number)
print("end")



