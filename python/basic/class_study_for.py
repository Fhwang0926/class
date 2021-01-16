#!/usr/bin/python // 파이썬을 위한 파일임을 선언
# -*- coding: utf8 -*- // 인코딩 방식 지정 => 한글 주석으로 인한 실행 에러 방지

# 반복문 : for     :  반복 횟수 예측 가능
#          while   : 반복 횟수 예측 불가능
# for : 사전에 또는 특정 상황에 맞춰서 미리 반복횟수 설정
# while : 특정 조건에 도달할 때까지 반복한다.

# for (초기값;조건식;증감값) --> for : 예측가능
# 파이썬 : 향상된 for문을 사용한다.

# for 변수 in 수열(리스트, 튜플)
# 파이썬에서 수열을 만들어내는 함수---> range()
# range(초기값;최종값;증감값)

# a = range(5)  --->  매개변수의 갯수 1개인 경우 : 최종값
# print(a)
# range(0, 5)   ---> 매개변수의 갯수 2개인 경우 : (초기값, 최종값)

# Code.01
for i in range(5):  # 반복횟수 : range수열의 갯수
    print(i)

# Code.02
for i in range(-1, 5):
    print(i)

# Code.03
for i in range(-1, 5, 2):
    print(i)

# Code.04
a = [1,2,4,6,8,9,2]
for i in a:
    print(i)

# Code.05
# 예제 

# 오락실 기계
# 1. for : 게임비용 500원 ---> 투입되는 동전의 값이 고정 100원
# 100원동전이 5번 투입되면 게임시작되는 프로그램
# 2. while : 게임비용 500원 ---> 투입되는 동전의 변동 (사용자 마음대로)

total = 500
coin = 100
sum = 0
money = 0
cnt = int(total/coin)
for i in range(cnt):
    money = int(input("동전을 투입해주세요:"))
    if money != 100:
        cnt = cnt - 1
        print("동전 좀 제대로 넣으세요(잘못 넣은 금액은 수수료)")
        continue
    sum = sum + money
    
if sum >= total:
    print("게임 시작")

# Code.06
# 리스트 내포(List comprehension)를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다
result = [x for x in range(1,10)]
print(result)

# Code.07
for i in range(1,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ") 
    print('')

# Code.08
for x in range(1, 10):
    print(x)
    print("빠져나가기")
    break