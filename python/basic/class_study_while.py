#!/usr/bin/python // 파이썬을 위한 파일임을 선언
# -*- coding: utf8 -*- // 인코딩 방식 지정 => 한글 주석으로 인한 실행 에러 방지

# 반복문 : for     :  반복 횟수 예측 가능
#          while   : 반복 횟수 예측 불가능
# for : 사전에 또는 특정 상황에 맞춰서 미리 반복횟수 설정
# while : 특정 조건에 도달할 때까지 반복한다.


# 사용법
# 초기값  ---> while 반복문에서 빠져나오기 위해 사용되는 변수
# while (조건문) : ---> 결과 : T / F
#     코드블럭      ---> 조건문의 값이 F가 될 때까지 계속 반복

# 코드블럭안에는 반드시 탈출조건과 관련이 있는 연산식이 필요하다.
# (증감값)

# while의 요소 : 초기값, 조건식, 증감식   : 동작 변수

# Code.01
a = True   # boolean 타입의 변수 --> 스위치변수
coffee = 10
money = 300
while a :
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    money = money - 100
    print("남은 커피의 양은 %d개입니다."% coffee)
    if coffee == 0:
        print("커피(돈)가 다 떨어졌습니다. 판매를 중지합니다.")
        a = False


# Code.02
a = True   # boolean 타입의 변수 --> 스위치변수
coffee = 10
money = 300
while a :
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    money = money - 100
    print("남은 커피의 양은 %d개입니다."% coffee)
    if coffee == 0:
        print("커피(돈)가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# Code.03
# continue : 코드블럭중에 continue문 바로 다음줄부터 skip
a = 0
while a < 10:
    a = a + 1
    if a%2 == 1:
        continue
    print(a)


# Code.04
total = 500
sum = 0
money = 0
while True:
    money = int(input("동전을 투입해주세요:"))
    sum = sum + money
    if (sum >= total):
        print("게임 시작")
        break

# Code.04
while True:
  # 작업 관리자 켜고 보세요, CPU 상태
  print("is not good")
  break


# Code.05
import time #  time 이라는 파이썬 기본 라이브러리 사용

while True: # 무한 반복에 빠지게 됨
  time.sleep(1)
  print("is good")
  break


# 무한 반복 활용 예시
# 챗봇

order = ""
method = ""
recive = ""
status = 1
while True:
  print("\n\n안녕하세요 야식의 민족입니다\n\n")
  print("="*20)

  if status == 1:
    print("메뉴 \n1. 짜장면\n2.짬뽕\n\n이 있습니다\n선택해주세요(1 or 2)")
    temp = input("메뉴를 입력하세요:")
    if temp == "1":
      order = "짜장면"
    else:
      order = "짬뽕"
    status = 2
    print("="*20)
  
  if status == 2:
    print("결제 방법 \n1. 카드\n2.현금\n\n이 있습니다\n선택해주세요(1 or 2)")
    temp = input("결제 방법을 입력하세요:")
    if temp == "1":
      method = "카드"
    else:
      method = "현금"
    status = 3
    print("="*20)
  
  if status == 3:
    print("수령 방법 \n1. 포장\n2.배달\n\n이 있습니다\n선택해주세요(1 or 2)")
    temp = input("수령 방법을 입력하세요:")
    if temp == "1":
      recive = "포장"
    else:
      recive = "배달"
    status = 1
    print("="*20)
  
  if order != "" and method != "" and recive != "":
    billing = "\n\n========주문내역=========\n"
    billing += "메뉴 : {0}\n".format(order)
    billing += "결제 방법 : {0}\n".format(method)
    billing += "수령 방법 : {0}\n".format(recive)
    billing += "=======================\n"
    print(billing)
    order = ""
    method = ""
    recive = ""
