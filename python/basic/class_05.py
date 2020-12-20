#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
import time

color = ['red', 'green', 'blue', 'black', 'white'] 

# list
print(color[0])
print(color[4])
print(color[1:4])


print('########')

# 범위로 생성
print(list(range(1,21, 2)))

# 한개씩 요소 활용
colors = ['빨간색', '파란색', '노란색', '검정색',  '초록색']
for color in colors:
    print('나는 %s을 가장 좋아합니다~~~' %  color)

print('########')

animals = ['사자', '호랑이',  '사슴', '곰']
i = 0
while i < len(animals):
    print(animals[i])
    i = i + 1

print('end')

# 삭제
member = ["황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678"]
print(member)
member.remove(20)
print(member)
print('end')

# 결합
member1 = ["황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678"]
member2 = ["황모씨", 20, "경기도 김포시", "b@google.com"]
print(member1 + member2)
print('end')

# 반복
member = ["황모씨", 20, "경기도 김포시", "a@google.com",  '123-1234-5678']
print(member * 2)
print('end')

# 정렬
member = [1, 3, 2, 5, 6, 4]
member.sort()
print(member)
print('end')

# 위치값
member = ["황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678"]
print(member.index(20))
print('end')

# 튜플 요소 접근
member = ("황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678")
print(member[0])
print(member[4])
print(member[1:4])
print('end')

# 튜플 결합
member1 = ("황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678")
member2 = ("황모씨", 20, "경기도 김포시", "a@google.com",  "123-1234-5678")
print(member1 + member2)
print('end')

# 딕셔너리
test = {}
test['key'] = 'value'
test['username'] = 'password'
print(test)
print('end')