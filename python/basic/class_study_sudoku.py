#!/usr/bin/python // 파이썬을 위한 파일임을 선언
# -*- coding: utf8 -*- // 인코딩 방식 지정 => 한글 주석으로 인한 실행 에러 방지

# 차원 개념
for i in range(1,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print("{0},{1}".format(i, j), end="|") 
    print('')

print("-"*30)

# 리스트 활용
main = [
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
  [1,2,3,4,5,6,7,8,9],
]
for x in main:        # ①번 for문
    for y in x:   # ②번 for문
        print("{0}".format(y), end="|") 
    print('')

print("-"*30)

# 스도쿠 형태 만들기
sudoku = []
index = 1
for row in main:
  r = []
  for num in range(index, 10):
    r.append(num)
  for num in range(10-len(r), 0, -1):
    r.append(num)
  sudoku.append(r)
  index += 1
  # sudoku

# 완성된 수도쿠 양식
print("-"*30)

for row in sudoku:
  for num in row:
    print(num, end="|")
  print('')

# 정답 저장후, 문제로 낼 부분 수정
print("-"*30)

answer = sudoku
sudoku[0][3] = 0
sudoku[6][3] = 0
sudoku[5][7] = 0

# 문제 확인
for row in sudoku:
  for num in row:
    print(num, end="|")
  print('')

# 빈칸 입력 받기(직접 구성)