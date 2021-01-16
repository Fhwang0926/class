#!/usr/bin/python // 파이썬을 위한 파일임을 선언
# -*- coding: utf8 -*- // 인코딩 방식 지정 => 한글 주석으로 인한 실행 에러 방지

# Code.01
# if문 ---> 조건문 --> 조건식을 활용 --> 조건식 : 연산의 결과((T/F))bool
# 연산 결과가 논리타입으로 나오는 연산자 --> 비교연산자
# 비교 연산자 : <, >, <=, >=, ==, !=

if 10 > 1:
    print("yes")
else:
    print("no")


if 10 != 1:
    print("yes")
else:
    print("no")

# Code.02
# 논리 연산자 :
# and, or, not,
# &&(&)    ||(|)    !(~)

# Code.03

if 10 == 10 && 10 == 10:
    print("yes")
else:
    print("no")

if 10 == 10 and 10 == 10:
    print("yes")
else:
    print("no")

# Code.04

# 어떠한 연산(비교나 논리 연산자를 활용한)이 수행된 간에 결과는 무조건 True / False

# 돈 : 기준   ---> 있으면 : True     ---> 택시
#                  없으면 : False    ---> 걸어간다.


me = "돈 있다"
if "돈 있다" == me:
    print("택시")
else:
    print("걸어간다")

money = False
if money :
    print("택시를 탑니다.") # 코드블럭 : money = True인 경우
else :
    print("걸어갑니다.")    # money = False 인 경우


# 1.돈의 기준 : 택시를 타기에 충분한 돈이 있는가?
#     목적지까지의 택비는 얼마 입니까? --> 5000
#     현재 자신이 가지고 있는 돈은 얼마 입니까? --> 4000


# Code.05

a = int(input("현재 당신이 갖고 있는 돈의 액수는?"))
cost = int(input("목적지까지의 택비는 얼마 입니까?"))
if a>=cost :
    money = True
else :
    money = False

if money :
    print("택시를 탑니다.") # 코드블럭 : money = True인 경우
else :
    print("걸어갑니다.")    # money = False 인 경우


# Code.06
# 2. 돈이 부족한 경우 ---> 1. 현금부족?
#                           --> 나에게 카드가 있다면?

a = int(input("현재 당신이 갖고 있는 돈의 액수는?"))
cost = int(input("목적지까지의 택비는 얼마 입니까?"))
money = False

if a>=cost :
    money = True
else :
    card = input("카드가 있나요?(yes/no)")
    if card == "yes":
        money = True
    elif card == "no" :
        money = False 
    else :
        print("잘못선택했내요.")
    
if money :
    print("택시를 탑니다.") # 코드블럭 : money = True인 경우
else :
    print("걸어갑니다.")    # money = False 인 경우


# Code.07

a = """
(워싱턴=연합뉴스) 이상헌 특파원 = 도널드 트럼프 미국 대통령은 5일(현지시간) 민주당이 선거를 훔치지 않는 한 자신이 이번 대선에서 이길 것이라고 말했다.

트럼프 대통령은 이날 오후 백악관에서 기자회견을 열고 "선거가 조작되고 있다"며 투표의 무결성을 지키는 것이 목표라고 언급했다.

그러면서 "합법적 투표만 계산하면 내가 쉽게 이긴다"면서 자신의 지지자들이 침묵하도록 두지는 않겠다고 말했다고 로이터통신은 전했다.

이는 조 바이든 민주당 후보가 막판 역전극을 연출하는 상황에서 선거인단 270명을 확보하더라도 불복하겠다는 의사를 밝힌 것으로 해석된다.

이와 관련해 트럼프 대통령은 이번 선거가 연방대법원에서 끝날 수도 있다고 언급, 최종적으로 법원의 판단을 받겠다는 입장을 밝혔다.

보수 절대 우위 구도인 연방대법원에서 최종 판단을 받겠다는 입장인 셈이다.

앞서 트럼프 대통령은 트위터에 글을 올려 바이든 후보가 승리를 주장하는 모든 주에서 법적으로 이의를 제기하겠다고 공언한 바 있다.

현재 바이든 후보는 선거인단 253명을 확보(애리조나 승리로 계산할 경우 264명)해 17명만 더 가져오면 승리한다. 트럼프 대통령은 214명을 확보한 상태다.
"""

b = a.split()
c = bool(b.count("트럼프"))
if c :
    if (b.count("트럼프")>=3):
        print("트럼프 관련도가 높은 기사")
    else :
        print("트럼프 관련도가 낮은 기사")
    
else :
    print("트럼프 관련 기사가 아닙니다.")



# Code.08
a = """
log파일 : IP 시간 동작
"""
b = a.count("IP")
if b >= 1000 :
    print("DOS공격이 의심됩니다.")

# Code.09

# if 사용법

# if 조건식 :
#     조건이 True인 경우 동작하는 코드블럭
# else :
#     조건이 False인 경우 동작하는 코드블럭

a = 8   # 100
b = 9   # 011
        # 000  ---> 비트 비교 연산 : 0   
print(bool(a and b))
#          -        : 4 --> T
#                 -  : 3 --> T    --> True : 비교연산자
print(a and b)   # b의 값이 출력됨


# Code.10


a = 8      # 1000
b = 9      # 1001
           # 1001   -> 9
print(bool(a or b))
print(a or b)   # a의 값이 출력됨


# Code.11
a = 9
print(bool(not a))    # !
print(not a)          # ~

# Code.12
# 돈 : 3000보다 많거나 카드가 있다면 택시
#               적거나 카드가 없다면 걸어간다.
# 3000보다 많거나 카드가 있다  : money >= 3000 or card == "yes"

a = ["핸드폰", "지갑", "시계"]
if "핸드폰" in a :
    if "지갑" in a :
        if "시계" in a :
            print("밖으로 나가자")
        else:
            print("나갈 수가 없어요")
    else :
        print("나갈 수가 없어요")
else:
    print("나갈 수가 없어요")

# Code.13
a = ["핸드폰", "지갑", "시계"]
if "핸드폰"in a and "지갑"in a and "시계"in a :
    print("밖으로 나가자")
else:
    print("나갈 수가 없어요")


# Code.14
a = ["핸드폰", "지갑", "시계"]
if "지갑1" not in a:
    print("나갈 수가 없어요")
    


# Code.15
# if 조건식 :
#     코드블럭 ---> 코드 테스트 --> 나중에 만들 예정

if money >= 5000 :
    pass

# if 조건1 :
#     코드블럭 : 조건1이 참인 경우
# elif 조건2 :
#     코드블럭 : 조건1이 거짓이면서 조건2가 참인 경우
# else:
#     코드블럭 : 조건1/조건2 모두 거짓인 경우 

# Code.16
# 문제 : 자판기 ----> 콜라 : 500원
#                     사이다 : 700원
#                     마운틴듀 : 1000원
#                     생수    : 2000원
#                     커피  : 300원

# 1. 메뉴 출력
# 2. 먹고 싶은 메뉴 선택 :  (숫자 / 문자)
# 3. 돈을 투입 --> input --> 문자
#                   int(input()) --> 숫자
# 4. if문을 사용해서 투입된 금액과 가격이 맞는 경우
# 5. 물건을 출력하고 거스름돈 출력

a = { 1 : ("콜라", 500), 2 : ("사이다", 700), 3 : ("마운틴듀", 1000), 4 : ("생수", 2000), 5 : ("커피", 300)}
print("메뉴판 출력")
b, c = a[1]
print("1. %s : %d원"% (b,c))
b, c = a[2]
print("2. %s : %d원"% (b,c))
b, c = a[3]
print("3. %s : %d원"% (b,c))
b, c = a[4]
print("4. %s : %d원"% (b,c))
b, c = a[5]
print("5. %s : %d원"% (b,c))

d = int(input("메뉴를 선택해주세요.(번호)"))
b, c = a[d]
print("당신이 선택한 메뉴는 %s이고 가격은 %d원입니다."% (b, c))

money = int(input("돈을 투입해주세요:"))
print("투입된 금액은 %d원 입니다."% money)

if money>=c :
    if c == money :
        print("주문하신 %s입니다."% b)
        print("안녕히가세요")
    else :
        print("주문하신 %s입니다."% b)
        print("잔액은 %d원 입니다." % (money-c))
        print("안녕히가세요")
else :
    print("투입된 금액이 %d원 부족합니다." % (c-money))

# 정리하고 들어가면
# if (조건식) :
#     코드블럭 ---> 조건식 --> T /F ---> True 코드블럭 실행
# else:
#     코드블럭 ---> 조건식 --> F --> 코드블럭 실행
# if 조건식1 :
#     코드블럭 1
# elif (조건식2) :
#     코드블럭 2
# elif (조건식3) :
#     코드블럭 3
# else :
#     코드블럭 4


# Code.17
pocket = ["지갑"]
print("지갑" in pocket)

# 조건부 표현식  ---> 자바 : 람다식 lambda
# 기본적으로 함수를 만들어서 사용하는 경우
#            ---                           : 같은 기능을 여러번 사용
if score>=60:
    message = "success"
else :
    message = "failure"
message = "success" if score>=60 else "failure"
