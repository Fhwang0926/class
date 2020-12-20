#!/usr/bin/python
# -*- coding: utf8 -*-
# auth : https://blog.naver.com/hdh0926
import time

# 함수 정의 및 사용
def hello():
    print('안녕하세요!')

hello()
print("end")

# 함수의 매개 변수
def customHello(x="안녕"):
    print(x)

customHello()
customHello(x="그래 안녕")
print("end")

# 함수 매개변수 활용
def test(start, end):
    hap = 0
    for i in range(start, end+1):
        hap = hap + i
        print('%d ~ %d의 정수의 합계 : %d' % (start, end, hap))

test(1, 10)
test(200, 200)
print("end")

# 함수 리턴값 활용
def function_hap(start, end):
    hap = 0
    for i in range(start, end+1):
        hap = hap + i
        print('%d ~ %d의 정수의 합계 : %d' % (start, end, hap))
    return hap


result = function_hap(200, 200) + function_hap(1, 10) - 5
print(result)
print("end")


# 파일 쓰기
file = open('sample.txt', 'w') 
for i in range(0, 3, 1): 
    print(i) 
    file.write(str(i))
file.close()
print("end")

# 파일 읽기
file = open('sample.txt', 'r') 
for i in file.readline(): 
    print(i) 
file.close()
print("end")


# 클래스 생성
class Room():
    status = 'clean'

    def __init__(self):
        print('new room')

    def clean(self):
        self.status = 'clean'

    def openPartry(self):
        self.status = 'not clean'

# 클래스로 객제 생성
room1 = Room() # Room 을 객체로 받은 room1 생성

print(room1)
print(room1.status)

# 파티를 해서 청소 필요
room1.openPartry() 
print(room1.status)

# 청소함
room1.clean()

# 이제 깨끗함
print(room1.status)
print('end')
